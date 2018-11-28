#pragma comment(linker,"/STACK:102400000,102400000")
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <ctime>
#include <cmath>
#include <cassert>
#include <stack>

#define MP make_pair
#define PB push_back
#define INF 1<<29
#define pii pair<int,int>
#define pll pair<LL,LL>
#define pdd pair<double,double>
#define vi vector<int>
#define L(x) x<<1
#define R(x) x<<1|1
#define SZ(x) (int)x.size()
#if(_WIN32||__WIN32__)
    #define LL __int64
    #define ll I64
#else
    #define LL long long
#endif
//#define Local

using namespace std;

int a[5][5];

int main()
{
	/*freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);*/
	int T,Case=0;
	scanf("%d",&T);
	while(T--)
	{
		vi v1,v2;
		int row;
		scanf("%d",&row);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		for(int j=0;j<4;j++)
			v1.PB(a[row-1][j]);
		scanf("%d",&row);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&a[i][j]);
		for(int j=0;j<4;j++)
			v2.PB(a[row-1][j]);
		int sum=0,ans=-1;
		for(int i=0;i<SZ(v1);i++)
		{
			for(int j=0;j<SZ(v2);j++)
			{
				if(v1[i]==v2[j])
				{
					sum++,ans=v1[i];
				}
			}
		}
		printf("Case #%d: ",++Case);
		if(sum==0)
			puts("Volunteer cheated!");
		else if(sum==1)
			printf("%d\n",ans);
		else
			puts("Bad magician!");
	}
	return 0;
}