#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;

template <class T>
void read(T &x)
{
	char ch;
	for (ch=getchar();(ch<'0'||ch>'9')&&ch!='-';) ch=getchar();
	x=0;int t=1;if (ch=='-') {ch=getchar();t=-1;}
	for (;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-'0';
	x*=t;
}

int pow2[20];
bool b[20][20];
int pre[1000],a[1000];

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int test;scanf("%d",&test);
	pow2[0]=1;for (int i=1;i<=16;i++) pow2[i]=pow2[i-1]<<1;
	for (int T=1;T<=test;T++)
	{
		printf("Case #%d:\n",T);
		int n,m;scanf("%d%d",&n,&m);
		for (int i=1;i<=2*(n+m);i++) scanf("%d",&a[i]);
		for (int i=1;i<=n+m;i++) {pre[a[2*i-1]]=a[2*i];pre[a[2*i]]=a[2*i-1];}
		bool ans=0;
		for (int i=0;i<pow2[n*m];i++)
		{
			for (int j=0;j<n;j++)
				for (int k=0;k<m;k++)
					if (i&pow2[j*m+k]) b[j][k]=1; else b[j][k]=0;
			bool ok=1;
			for (int i=1;i<=2*(n+m);i++)
			{
				int x,y,d;
				if (i<=m) {x=0;y=i-1;d=0;}
				if (i>m&&i<=n+m) {x=i-m-1;y=m-1;d=1;}
				if (i>n+m&&i<=n+2*m) {x=n-1;y=n+2*m-i;d=2;}
				if (i>n+2*m) {x=2*(n+m)-i;y=0;d=3;}
				while (x>=0&&x<n&&y>=0&&y<m)
				{
					if (b[x][y])
					{
						if (d==0)
						{
							y--;d=1;
						}
						else
							if (d==1)
							{
								x++;d=0;
							}
							else
								if (d==2)
								{
									y++;d=3;
								}
								else
								{
									x--;d=2;
								}
					}
					else
					{
						if (d==0)
						{
							y++;d=3;
						}
						else
							if (d==1)
							{
								x--;d=2;
							}
							else
								if (d==2)
								{
									y--;d=1;
								}
								else
								{
									x++;d=0;
								}
					}
				}
				int t;
				if (x==-1) t=y+1;
				if (y==m) t=x+m+1;
				if (x==n) t=2*m+n-y;
				if (y==-1) t=2*(m+n)-x;
				if (pre[i]!=t) {ok=0;break;}
			}
			if (ok)
			{
				for (int i=0;i<n;i++)
				{
					for (int j=0;j<m;j++) if (b[i][j]) putchar('/'); else putchar(92);
					puts("");
				}
				ans=1;break;
			}
		}
		if (!ans) puts("IMPOSSIBLE");
	}
	return 0;
}

