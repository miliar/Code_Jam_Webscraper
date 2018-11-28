#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
int c[3010];
int pp[3010*3010];
int qq;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n;
		scanf("%d",&n);
		memset(c,0,sizeof(c));
		for(int i=0;i<n+n-1;i++)
			for(int j=0;j<n;j++)
			{
				int s;
				scanf("%d",&s);
				c[s]^=1;
			}
		qq=0;
		for(int i=0;i<3000;i++)
			if(c[i] == 1)
				pp[qq++]=i;
		printf("Case #%d:",cc);
		for(int i=0;i<qq;i++)
			printf(" %d",pp[i]);
		printf("\n");
	}
    return 0;
}
/*
1
3
1 2 3
2 3 5
3 5 6
2 3 4
1 2 3

 */
