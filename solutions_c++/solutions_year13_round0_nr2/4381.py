#include <cstdio>
#include <cstring>

using namespace std;

int m,n;
int a[100][100];
bool ans;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	scanf("%d", &t);
	for (int ii = 1; ii <= t; ++ii)
	{
		ans=true;
		scanf("%d%d", &n,&m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				scanf("%d", &a[i][j]);

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				bool tl1=true,tl2=true;
				for (int k = 0; k < n; ++k)
					tl1&=a[k][j]<=a[i][j];				
				for (int k = 0; k < m; ++k)
					tl2&=a[i][k]<=a[i][j];
				ans&=tl1||tl2;
			}

		printf("Case #%d: ", ii);
		if(ans)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}