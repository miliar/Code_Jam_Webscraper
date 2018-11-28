#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include <string>
#include <sstream>

using namespace std;

int MAX(size_t& a, size_t& b)
{
	if(a > b)
		return a;
	else
		return b;
}

int main(int argc, char* argv[])
{
	ifstream inf(argv[1]);
	assert(inf.is_open());
	string line;

	getline(inf, line);
	size_t** yard;
	size_t** newyard;
	size_t T = atoi(line.c_str());
	for(size_t t=0; t<T; t++)
	{
		size_t N, M;
		getline(inf, line);
		sscanf((char*) line.c_str(),"%ld %ld\n", &N, &M);

		yard = new size_t*[N];
		newyard = new size_t*[N];
		size_t begin = 0, index = 0;
		for(size_t i=0; i<N; i++)
		{
			yard[i] = new size_t[M];
			newyard[i] = new size_t[M];
			getline(inf, line);
			size_t begin = 0, index = 0;
			for(size_t j=0; j<M; j++)
			{
				newyard[i][j] = 100;
				index = line.find(" ");
				if(index != string::npos)
				{
					string str_num = line.substr(0, index);
					yard[i][j] = atoi((char*)str_num.c_str());
				}
				else
					yard[i][j] = atoi((char*) line.c_str());

				line = line.substr(index+1, line.length()-index);
			}
		}

		size_t* row_h = new size_t[N];
		size_t* col_h = new size_t[M];
		
		for(size_t i=0; i<N; i++)
		{
			row_h[i] = 0;
			for(size_t j=0; j<M; j++)
			{
				row_h[i] = MAX(row_h[i], yard[i][j]);
			}
			for(size_t j=0; j<M; j++)
			{
				if(newyard[i][j] > row_h[i])
					newyard[i][j] = row_h[i];
			}
		}
		for(size_t i=0; i<M; i++)
		{
			col_h[i] = 0;
			for(size_t j=0; j<N; j++)
			{
				col_h[i] = MAX(col_h[i], yard[j][i]);
			}
			for(size_t j=0; j<N; j++)
			{
				if(newyard[j][i] > col_h[i])
					newyard[j][i] = col_h[i];
			}
		}

		bool issucc = true;
		for(size_t i=0; i<N; i++)
		{
			for(size_t j=0; j<M; j++)
			{
				if(yard[i][j] != newyard[i][j])
				{
					issucc = false;
					break;
				}
			}
			if(issucc == false)
				break;
		}
		if(issucc)
		{
			cout<<"Case #"<<t+1<<": "<<"YES"<<endl;
		}
		else
		{
			cout<<"Case #"<<t+1<<": "<<"NO"<<endl;
		}

		
		for(size_t i=0; i<N; i++)
		{
			delete [] yard[i];
			delete [] newyard[i];
		}
		delete [] yard;
		delete [] newyard;
		delete [] row_h;
		delete [] col_h;
	}
	inf.close();	
	return 0;
}

