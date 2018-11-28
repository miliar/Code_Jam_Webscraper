#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>
#include<map>
#include<cstdio>
#include<stack>
#include<cstring>
#include<climits>
#include<cmath>
#include<queue>
#include<string>

using namespace std;


int main()
{
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
		bool isPossible = true;
		int n,m;
		cin>>n>>m;
		int data[101][101], row[101], col[101];
		memset(row, -1, sizeof(row));
		memset(col, -1, sizeof(col));

		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				cin>>data[i][j];
				row[i] = max(row[i], data[i][j]);
				col[j] = max(col[j], data[i][j]);
			}
		}

		
		for(int i=0;isPossible && i<n; i++)
		{
			for(int j=0;isPossible && j<m; j++)
			{
				if(data[i][j] < row[i] && data[i][j]<col[j])
				{
					isPossible = false;
				}
			}
		}
		printf("Case #%d: %s\n",cas, (isPossible? "YES":"NO"));
	}
	return 0;
}