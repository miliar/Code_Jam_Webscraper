#include<iostream>
#include<cstdio>

using namespace std;

const int maxn=1100;
int num,ca,n,m;
int a[maxn][maxn];
void init()
{
	cin>>num;
	while (num--)
	{
		cin>>n>>m;
		for (int i=1; i<=n; i++)
			for (int j=1; j<=m; j++) cin>>a[i][j];
		
		bool ans=true;
		for (int i=1; i<=n; i++)
			for (int j=1; j<=m; j++)
			{
				bool pp=true;
				int tot=0;
				for (int l=1; l<=n; l++) 
					if (a[i][j]<a[l][j]) pp=false;

				if (pp) ++tot;

				pp=true;
				for (int l=1; l<=m; l++)
					if (a[i][j]<a[i][l]) pp=false;

				if (pp) ++tot;

				if (tot==0) ans=false;
			}

		if (ans) printf("Case #%d: YES\n",++ca); else printf("Case #%d: NO\n",++ca);
	}
}
int main()
{
	freopen("bbb.in","r",stdin);
	freopen("bbb.out","w",stdout);
	init();
	return 0;
}
