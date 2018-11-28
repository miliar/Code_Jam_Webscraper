#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

//istream& fin = cin;
//ifstream fin ("B-sample.txt");
ifstream fin ("B-small-attempt1.in");
ofstream fout ("B-small-attempt1.out");
//ifstream fin ("B-large.in");
//ofstream fout ("B-large.out");
//ostream& fout = cout;

int n,m;
int map[100][100];
int rowMax[100];
int colMax[100];

bool possible()
{
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			if(map[i][j] < rowMax[i] && map[i][j] < colMax[j])
			{				
				return false;
			}			
		}
	}
	return true;
}

int main()
{
	int N;
	fin >> N;
	for(int k=1; k<=N; k++)
	{
		fin >> n >> m;
		
		std::fill(colMax,colMax+m,0);
		for(int i=0; i<n; i++)
		{
			rowMax[i]=0;
			
			for(int j=0; j<m; j++)
			{
				fin >> map[i][j];
				//fout << map[i][j] << ' ';
				if(map[i][j] > rowMax[i])
					rowMax[i]=map[i][j];
				if(map[i][j] > colMax[j])		
					colMax[j]=map[i][j];
			}
			//fout << endl;
		}
		if(possible())
		{
			fout << "Case #" << k << ": YES" << endl;
		}
		else
		{
			fout << "Case #" << k << ": NO" << endl;
		}
	}
	
	return 0;
}

