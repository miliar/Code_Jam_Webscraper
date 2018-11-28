#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

  
int main()
{
	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("C-large-1.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	//freopen("B.txt", "w", stdout);
	int t;
	cin>>t;
	int lawn[101][101];
	int result;
	for(int k=0; k<t; k++)
	{
		int n, m;
		cin>>n>>m;
		int min = 101;
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				cin>>lawn[i][j];
				if(lawn[i][j] < min)
					min = lawn[i][j];
			}
		}
		result = 1;
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				int sign = 0;
				
				for(int x=0; x<n; x++)
				{
					if(lawn[i][j] < lawn[x][j])
					{
						sign++;
						break;
					}
				}
				for(int x=0; x<m; x++)
				{
					if(lawn[i][j] < lawn[i][x])
					{
						sign++;
						break;
					}
				}
			
				if(sign == 2)
					result = 0;
			}
		}
		if(result == 1)
			printf("Case #%d: YES\n", k+1);
		else
			printf("Case #%d: NO\n", k+1);
	}


	fclose(stdout);
	fclose(stdin);
	return 0;
}

