#include <iostream>
#include <cstdio>

using namespace std;

#define rep(i,n) for (int n__=n,i=1;i<=n__;i++)

#define repb(i,b,n) for (int n__=n,i=(b);i<=n__;i++)

char a[55][55];
int n,m,k,sf;

void out()
{
	a[1][m]='c';
	if (sf)
		rep(i,m)
		{
			rep(j,n)
				printf("%c",a[j][i]);
			putchar('\n');
		}
	else
	{
		rep(i,n)
		{
			rep(j,m)
				printf("%c",a[i][j]);
			putchar('\n');
		}
	}
}

void imp()
{
	puts("Impossible");
}

void error()
{
	puts("error!______________________________________________\n");
}

int main()
{
	freopen("D:\\inout\\gcj3b.in","r",stdin);
	freopen("D:\\inout\\gcj3b.out","w",stdout);
	int z;
	cin>>z;
	rep(zz,z)
	{
		printf("Case #%d:\n",zz);
		cin>>n>>m>>k;
		if (n>=m)
			sf=0;
		else
			sf=1,swap(n,m);
		k=n*m-k;
		rep(i,n)
			rep(j,m)
				a[i][j]='*';
		if (k==1)
		{
			out();
			continue;
		}
		else
		if (m==1)
		{
			if (k>=2)
			{
				rep(i,k)
					a[i][1]='.';
				out();
				continue;
			}
			error();
		}
		else
		if (m==2)
		{
			if (k>=4 && k%2==0)
			{
				rep(i,k/2)
					rep(j,m)
						a[i][j]='.';
				out();
				continue;
			}
			else
			{
				imp();
				continue;
			}
		}
		else
		if (m>=3)
		{
			if (k==7 || k==5 || k==3 || k==2)
			{
				imp();
				continue;
			}
			rep(i,2)
				rep(j,m)
					a[i][j]='.';
			repb(i,3,n)
				repb(j,m-1,m)
					a[i][j]='.';
			int v=n*m-(n-2)*(m-2)-k;
			k=n*m-k;
			if (k>(n-2)*(m-2))
				k=(n-2)*(m-2);
			if (v>0 && v%2==1)
			{
				v+=1;
				k-=1;
			}
			{
				for (int i=n;i>=4;i--)
					repb(j,m-1,m)
					if (v>0)
					{
						a[i][j]='*';
						v--;
					}
			}
			{
				rep(i,m-2)
					rep(j,2)
					if (v>0)
					{
						a[j][i]='*';
						v--;
					}
			}
			if (v>0)
			{
				a[3][m-1]='*';
				a[3][m]='*';
			}

			if (k<(n-2)*(m-2))
			{
				k=(n-2)*(m-2)-k;
				repb(i,3,n)
					for (int j=m-2;j>=1;j--)
						if (k>0)
						{
							a[i][j]='.';
							k--;
						}
			}
			out();
			continue;
		}
		error();
	}
}
