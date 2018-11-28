/*
._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._
	ABHINANDAN AGARWAL
	MNNIT ALLAHABAD
	CSE
._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._
*/
#include<bits/stdc++.h>
using namespace std;
#define pc putchar_unlocked
#define gc getchar_unlocked
typedef long long ll;
typedef unsigned long long llu;
#define mp make_pair
#define pb push_back
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define scstr(x) scanf("%s",x)
#define pd(x) printf("%d",x)
#define pstr(x) printf("%s",x)
#define newl() printf("\n")
#define fl(i,n) for (i=0;i<n;i++)
#define fle(i,n) for (i=1;i<=n;i++)
#define fla(i,a,n) for (i=a;i<n;i++)
#define mem(a,i) memset(a,i,sizeof(a))
#define fi first
#define se second
typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > piii ;
#define wl(n) while (n--)
#define MOD 1000000007
//-------------
int A[100][100]={0};
int main()
{
	int t;
	sc(t);int ass=1;
	wl(t)
	{
		int n;ll m;
		printf("Case #%d: ",ass);
		ass++;
		sc(n);scanf("%lld",&m);
		int i;
		ll x=1;
		for (i=0;i<n-2;i++)
			x*=2;
		if (m>x)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		printf("POSSIBLE\n");
		if ((m&(m-1))==0&&m==x)
		{
			for (i=0;i<n;i++)
			{
				printf("%d",i==0?0:1);
			}
		}
		else
		{
			for (i=0;i<n;i++)
			{
				if (n-i-2>=0&&((1LL<<(n-i-2))&m))
					printf("1");
				else printf("0");
			}
		}
		printf("\n");
		for (i=1;i<n;i++)
		{
			int j;
			for (j=0;j<n;j++)
			{
				if (j>i)
					printf("1");
				else
					printf("0");
			}
			printf("\n");
		}
		
	}		

	return 0;

}