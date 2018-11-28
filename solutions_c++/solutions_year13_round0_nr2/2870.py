#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>

using namespace std;

int max(int a, int b)
{
	return (a>b) ? a : b;
}

struct lawn
{
	vector< vector<int> > config;

	lawn(vector< vector<int> > con) : config(con) {};

	int max_r(int n)//row number
	{
		int maximum = config[n][0];
		for(unsigned i=1;i<config[n].size();i++)
		{
			maximum = max(maximum, config[n][i]);
		}
		return maximum;
	}

	int max_c(int n)//column number
	{
		int maximum = config[0][n];
		for(unsigned i=1;i<config.size();i++)
		{
			maximum = max(maximum, config[i][n]);
		}
		return maximum;
	}

	bool good(int x, int y)
	{
		int num = config[x][y];
		return (num >= max_r(x)) || (num >= max_c(y));
	}

	bool good()
	{
		for(unsigned i=0;i<config.size();i++)
		{
			for(unsigned k=0;k<config[0].size();k++)
			{
				if(!good(i,k))
					return false;
			}
		}
		return true;
	}

	void print()
	{
		for(unsigned i=0;i<config.size();i++)
		{
			for(unsigned k=0;k<config[i].size();k++)
			{
				cout<<config[i][k]<<" ";
			}
			cout<<endl;
		}
	
	}

};

vector< vector<int> > get_array(ifstream& fin, int N, int M)
{
	vector< vector<int> > answer;
	for(int i=0;i<N;i++)
	{
		vector<int> line;
		for(int k=0;k<M;k++)
		{
			int temp;
			fin>>temp;
			line.push_back(temp);
		}
		answer.push_back(line);
	}
	return answer;
}

int main()
{
	ifstream fin("lawnmower.in");
	int T;
	fin>>T;

	ofstream fout("lawnmower.out");

	for(int i=0;i<T;i++)
	{
		int N,M;
		fin>>N>>M;

		lawn l(get_array(fin, N, M));
		//cout<<"Case #"<<(i+1)<<": "<<endl;
		//l.print();
		//cout<<endl;
		fout<<"Case #"<<(i+1)<<": ";
		fout<<((l.good()) ? "YES" : "NO");
		fout<<endl;
	}

	return 1;
}
