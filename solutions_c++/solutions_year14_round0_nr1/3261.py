#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>

#define SQR(_x) ((_x)*(_x))
//#define REP(_i,_n) for(int _i = 0; _i < (int)(_n); _i++)
//#define FOR(_i,_a,_b) for(int _i = (int)(_a); _i <= (int)(_b); _i++)
//#define BCK(_i,_a,_b) for(int _i = (int)(_a); _i >= (int)(_b); _i--)
#define NL printf("\n")
#define LL long long
#define INF 1000000000

using namespace std;

int mem[17]={};
int row[17]={};
int cnt=0;
int ans;

int main()
{
	int n,m,t,q;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)
	{
		q=2;
		for(int j = 1; j <= 16; j++)
		{
			mem[j]=0;
			row[j]=0;
		}
		cnt=0;
		while(q--)
		{
			scanf("%d",&m);
			for(int j = 1; j <= 4; j++)
			{
				for(int k = 1; k <= 4; k++)
				{
					scanf("%d",&n);
					if(j==m)
					{
						mem[n]++;
						row[n]=k;
						if(mem[n]==2)
						{
							if(q==0 and row[n]==k)
							{
								ans = n;
							}
							cnt++;
						}
					}
				}
			}
		}
		if(cnt==1)
			printf("Case #%d: %d\n",i,ans);
		else if(cnt>1)
			printf("Case #%d: Bad magician!\n",i);
		else
			printf("Case #%d: Volunteer cheated!\n",i);
	}
	return 0;
}