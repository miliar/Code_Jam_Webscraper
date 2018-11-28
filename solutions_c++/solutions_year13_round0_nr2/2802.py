#include<cstdio>
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ofstream myfile;
	myfile.open ("lawn.out");
	int t, c=1;
	scanf("%d", &t);

	while(t--)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		int g[n][m];
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				scanf("%d", &g[i][j]);
		int flag=1;
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				if(g[i][j] == 1)
				{
					flag = 2;
					for(int k=0; k<m; k++)
						if(g[i][k] != 1)
						{
							flag--;
							break;
						}
					for(int k=0; k<n; k++)
						if(g[k][j] != 1)
						{
							flag--;
							break;
						}

					if(!flag)
						break;
				}
			}
			if(!flag)
				break;
		}
		if(!flag)
			myfile << "Case #"<< c << ": NO" << endl;
		else
			myfile << "Case #"<< c << ": YES" << endl;
		c++;
	}
	return 0;
}
