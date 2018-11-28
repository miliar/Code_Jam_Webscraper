#include <cstdio>
#include<algorithm>
#include <queue>
#include <iostream>

#define FORN(i,a,b) for (int i = (a); i <= (b); i++)
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define S ({int x; scanf("%d%*c", &x); x;})
#define PN(x) ({printf("%d\n", x);})
#define PS(x) ({printf("%d ", x);})
#define NL ({printf("\n");})
#define printarr(i, x, y) ({for(int i=0;i<y;i++){ printf("%d ", x[i]);} printf("\n");})
#define inputarr(i, x, y) ({for(int i=0;i<y;i++){ scanf("%d", &x[i]);}})
#define MOD 1000000007
#define LL long long

using namespace std;
int main()
{
	int n5;
	n5=S;
	int casenum=1;
	while(n5--)
	{
		unsigned LL r, t, x,y,ans=0,num,sum=0;
		scanf("%llu%llu", &r, &t);
		unsigned LL i=1;
			while(1)
			{
				num = 2*r+2*i-1;
				sum+=num;
				if(sum<=t)
					ans+=1;
				else
					break;
				i+=2;
			}
		printf("Case #%d: %llu\n", casenum, ans);
		casenum++;
	}
	return 0;
}

