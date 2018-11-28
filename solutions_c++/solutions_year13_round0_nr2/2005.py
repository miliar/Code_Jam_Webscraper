#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#define pb push_back
#define mp make_pair
#define ST begin()
#define ED end()
#define x first
#define y second
#define elif else if 
#define foreach(i,x) for (__typeof((x).ST) i=(x).ST;i!=(x).ED;++i) 
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vci;
typedef vector<string> vcs;
typedef pair<int,int> PII;

const int N = 105;

int task, n, m;
int a[N][N], c[N][N];
pair<int, PII> b[N*N];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int task;
	scanf("%d", &task);
	for (int _i=1;_i<=task;++_i)
	{
		scanf("%d%d", &n, &m);
		int t=0;
		for (int i=1;i<=n;++i)
			for (int j=1;j<=m;++j)
			{
				scanf("%d", &a[i][j]);
				b[++t]=mp(a[i][j],mp(i,j));
				c[i][j]=100;
			}
		sort(b+1,b+t+1);
		int ans=1;
		for (int i=t;i>=1;--i)
		{
			int x=b[i].y.x,y=b[i].y.y,z=b[i].x;
			if (z<c[x][y])
			{
				int ok=1;
				for (int j=1;j<=m;++j)
					if (j!=y&&a[x][j]>z)
					{
						ok=0;
						break;
					}
				if (ok)
				{
					for (int j=1;j<=m;++j)
						c[x][j]=z;
					continue;
				}
				ok=1;
				for (int j=1;j<=n;++j)
					if (j!=x&&a[j][y]>z)
					{
						ok=0;
						break;
					}
				if (ok)
				{
					for (int j=1;j<=n;++j)
						c[j][y]=z;
					continue;
				}
				ans=0;
				break;
			}
		}
		if (ans)
			printf("Case #%d: YES\n", _i);
		else
			printf("Case #%d: NO\n", _i);
	}

	return 0;
}
