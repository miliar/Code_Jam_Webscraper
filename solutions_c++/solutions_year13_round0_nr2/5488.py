#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int ro[110],co[110];
int a[110][110];
int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	int T;cin >> T;
	for(int cases = 1;cases <= T; ++cases)
	{
		int n,m;
		cin >> n >> m;
		memset(ro,0,sizeof(ro));
		memset(co,0,sizeof(co));
		for(int i = 0;i < n; ++i)
			for(int j = 0;j < m; ++j)
			{
				cin >> a[i][j];
				ro[i] = max(ro[i],a[i][j]);
				co[j] = max(co[j],a[i][j]);
			}
		bool ans = 1;
		for(int i = 0;i < n; ++i)
			for(int j = 0;j < m; ++j)
				ans = ans && (ro[i]==a[i][j] || co[j]==a[i][j]);
		printf("Case #%d: ",cases);
		if(ans)
			printf("YES\n");
		else
			printf("NO\n");
	}
}
