using namespace std;
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>

typedef long long L;
typedef unsigned long long U;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;

main()
{
	int tc;
	cin>>tc;
	for(int t = 1;t<=tc;t++)
	{
		int f,s, arr1[4][4], arr2[4][4];
		scanf("%d", &f);
		for(int i = 0;i<4;i++)
		{
			for(int j = 0;j<4;j++)
				scanf("%d", &arr1[i][j]);
		}
		scanf("%d", &s);
		for(int i = 0;i<4;i++)
		{
			for(int j = 0;j<4;j++)
				scanf("%d", &arr2[i][j]);
		}
		f--;
		s--;
		int x = 0;
		for(int i = 0;i<4;i++)
		{
			for(int j = 0;j<4;j++)
			{
				if(arr1[f][i] == arr2[s][j])
				{
					if(x == 0)
						x = arr1[f][i];
					else
						x = -1;
				}
			}
		}
		if(x == 0)
			printf("Case #%d: Volunteer cheated!\n", t);
		else if(x == -1)
			printf("Case #%d: Bad magician!\n",t);
		else
			printf("Case #%d: %d\n", t, x);
	}
}
