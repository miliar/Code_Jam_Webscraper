#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)

typedef long long ll;

const int MAXN=20000;
int a[MAXN];

int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		int n,x;
		scanf("%d%d",&n,&x);
		REP(i,n)
			scanf("%d",&a[i]);
		sort(a,a+n);
		int lp=0;
		int rp=n-1;
		int cnt=0;
		while(lp<rp)
		{
			if(a[lp]+a[rp]<=x)
			{
				lp++;
				rp--;
				cnt++;
			}
			else
				rp--;
		}
		printf("Case #%d: %d\n",test,n-cnt);
	}
	return 0;
}
