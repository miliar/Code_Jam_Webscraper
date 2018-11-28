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
char s[100000];
char xx[100000];
int main()
{
	int t;
	sc(t);int ass=1,i;
	wl(t)
	{
		scstr(s);
		int l=strlen(s);
		printf("Case #%d: ",ass);
		ass++;
		int st=50000,en=49999,p=0;
		for (i=0;i<l;i++)
		{
			if (s[i]>=s[p])
			{
				xx[--st]=s[i];
				p=i;
			}
			else
			{
				xx[++en]=s[i];
			}

		}
		for (i=st;i<=en;i++)
		{
			printf("%c",xx[i]);
		}
		printf("\n");

	}

	return 0;

}