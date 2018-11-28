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
int yo(ll x,int *hs)
{
	while (x)
	{
		hs[x%10]++;
		x/=10;
	}
	int i;
	for (i=0;i<10;i++)
	{
		if (hs[i]==0)
			return 0;
	}
	return 1;
}
int main()
{
	int t,ass=0;
	sc(t);
	wl(t)
	{
		ll n,i,j;
		ass++;
		int hs1[10]={0};
		scanf("%lld",&n);
		printf("Case #%d: ",ass);
		if (n==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		for (i=1;1;i++)
		{
			if (yo(i*n,hs1))
				break;
		}
		printf("%lld\n",i*n);
	}		

	return 0;

}