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
char s[210];
int main()
{
	int t,ass=0;
	sc(t);
	wl(t)
	{
		ass++;
		scanf("%s",s);
		int l=strlen(s),i,j;
		printf("Case #%d: ",ass);
		int ans=0;
		for (i=l-1;i>=0;i--)
		{
			if (s[i]=='+')
				continue;
			for (j=0;j<i;j++)
				if (s[j]!='+')
					break;
			ans+=(j>0?1:0);
			int k;
			for (k=0;k<j;k++)
				s[k]=(s[k]=='+'?'-':'+');
			for (k=0;k<=i;k++)
				s[k]=(s[k]=='+'?'-':'+');
			int a=0,b=i;
			while (a<b)
			{
				swap(s[a],s[b]);a++;b--;
			}
			ans++;
		}
		printf("%d\n",ans);
	}		

	return 0;

}