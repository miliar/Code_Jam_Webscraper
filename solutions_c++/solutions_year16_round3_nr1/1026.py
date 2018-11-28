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
int A[100];
int main()
{
	int t;
	sc(t);int ass=1;
	wl(t)
	{
		printf("Case #%d: ",ass);
		ass++;
		int n,i,j;
		sc(n);
		for (i=0;i<n;i++)
		{
			sc(A[i]);
		}
		int mx,ele;
		while (1)
		{
			for (i=0;i<n;i++)
			{
				
				if (A[i]==0)
					continue;
				A[i]--;
				for (j=-1;j<n;j++)
				{
					if (j!=-1)
						A[j]--;
					int k;mx=0;int lg=0;
					for (k=0;k<n;k++)
					{
						if (mx<A[k])
						{
							mx=A[k];
							ele=k;
						}
						lg+=A[k];
					}

					if (j!=-1)
						A[j]++;
					//printf("%d,%d %d ele:%d and mx:%d\n",i,j,lg,ele,mx);
					if (mx<lg/2+(lg%2==0))
					{
						if (j!=-1)
							printf("%c%c ",i+'A',j+'A');
						else printf("%c ",i+'A');
						A[i]-=1;
						if (j!=-1)A[j]-=1;
					}
				}
				A[i]++;
			}
			for (i=0;i<n;i++)
			{
				if (A[i]!=0)break;
			}
			if (i==n)
				break;

		}
		printf("\n");
	}

	return 0;

}