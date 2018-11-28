#include <iostream>
#include <fstream>
#include <math.h>
#include <sstream>
#include <cstdlib>
#include <vector>
using namespace std;

int main()
{
	int cases,n,m,lawn[100][100]={100};
	string line,temp;
	freopen("B-small-attempt1.in","rt",stdin);
	freopen("B-small-attempt1.out","wt",stdout);
	cin>>cases;
	getline(cin,line);
	for (int i=0; i < cases ; i++)
	{
		int j=0;
		bool yes=true;
		vector<vector<int>> lawn1(100,vector<int>(100,100));
		int lawn_r[100][100],row[100]={0},col[100]={0};
		getline(cin,line);
		stringstream ss(line);
		while (ss>>temp)
		{
			if(j==0)
				n=atoi( temp.c_str());
			else
				m=atoi( temp.c_str());
			j++;
		}

		for (int a = 0; a < n; a++)
		{
			/*row[a][0]=a;
			row[a][1]=0;
			row[a][2]=lawn[a][0];*/
			getline(cin,line);
			stringstream ss1(line);
			for (int b = 0; b < m; b++)
			{
				ss1 >> temp;
				lawn_r[a][b]= atoi(temp.c_str());
				if (lawn_r[a][b] > row[a])
				{
					row[a]=lawn_r[a][b];
				}
				/*if (lawn_r[b][a]>col[b][2])
				{
				col[a][0]=a;
				col[a][1]=b;
				col[a][2]=lawn_r[a][b];
				}*/

			}
		}

		for (int x = 0; x < n; x++)
		{
			for (int y = 0; y < m; y++)
			{
				if (lawn1[x][y]>row[x])
				{
					lawn1[x][y]=row[x];
				}
			}
		}
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (lawn_r[j][i]>col[i])
				{

					col[i]=lawn_r[j][i];
				}
			}
		}
		for (int z = 0; z < n; z++)
		{
			for (int x = 0; x < m; x++)
			{
				if (lawn1[z][x]>col[x])
				{
					for (int y = 0; y < n; y++)
					{
						lawn1[y][x]=col[x];

						/*if (lawn1[x][y]>col[x][2])
						{
						col[x][0]=x;
						col[x][1]=y;
						col[x][2]=lawn1[x][y];
						}*/
					}
				}
				//cout<<col[x][2]<<" ";
			}
		}
		cout<<"Case #"<<i+1<<": ";
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if(lawn1[i][j]!=lawn_r[i][j])
				{
					yes=false;
				}
			}
		}
		if (yes)
		{
			cout<<"YES\n";
		}
		else
		{
			cout<<"NO\n";
		}
	}
	return 0;

}