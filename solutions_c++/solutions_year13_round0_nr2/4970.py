#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int maximum(int* input, int n)
{
	int m = -1;
	for(int i=0; i<n; i++)
		if(input[i]>m)
			m = input[i];
	return m;
}
bool check(int** input, int m, int n)
{
	int *row = new int [m];
	int *col = new int[n];
	for(int i=0; i<n; i++)
		col[i] = -1;
	
	for(int i=0; i<m; i++)
	{
		row[i] = maximum(input[i], n);
		for(int j=0; j<n; j++)
			if(input[i][j]>col[j]) col[j] = input[i][j];
	}

	for(int i=0; i<m; i++)
		for(int j=0; j<n; j++)
			if(input[i][j] != row[i] && input[i][j] != col[j])
				return false;
	return true;
}

int main()
{
	ofstream youfile("output.txt");
	int** input;
	char * temp=new char[100];
	string line, strnum, strmn;
	int size, m, n;
	ifstream myfile ("B-large.in");
	if (myfile.is_open())
	{
		getline (myfile, strnum);
		size = atoi(strnum.c_str());

		for(int k=0; k<size; k++)
		{
			getline (myfile, strmn);
			strcpy(temp, strmn.c_str());
			m = atoi(strtok(temp, " "));
			n = atoi(strtok(NULL, " "));
			input = new int*[m];
			for(int i=0; i<m; i++)
			{
				input[i] = new int[n];
				getline (myfile, line);
				strcpy(temp, line.c_str());
				input[i][0] = atoi(strtok(temp, " "));
				for(int j=1; j<n; j++)
				{
					input[i][j] = atoi(strtok(NULL, " "));
				}
			}
		
			if(check(input, m, n))
				youfile<<"Case #"<<k+1<<": YES"<<endl;
			else
				youfile<<"Case #"<<k+1<<": NO"<<endl;
		}
		myfile.close();
	}

	system("pause");
}