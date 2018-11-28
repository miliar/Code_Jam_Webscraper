#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <map>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-9
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long

using namespace std;

int T, row[2];
int conf[2][4][4];

int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		for(int i = 0; i < 2; i++)
		{
			scanf("%d", &row[i]); row[i]--;
			for(int j = 0; j < 4; j++)
				for(int k = 0; k < 4; k++)
					scanf("%d", &conf[i][j][k]);
		}
		
		int cnt = 0, ans = -1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(conf[0][row[0]][i] == conf[1][row[1]][j])
				{
					cnt++;
					ans = conf[0][row[0]][i];
				}
				
		printf("Case #%d: ", t);
		if(cnt == 1) printf("%d\n", ans);
			else if(cnt == 0) printf("Volunteer cheated!\n");
				else if(cnt > 1) printf("Bad magician!\n");
				
	}
	return 0;
}

