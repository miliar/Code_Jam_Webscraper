#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

void Work(int Case)
{
	static bool Vis[15];
	memset(Vis,0,sizeof Vis);
	int n;
	scanf("%d", &n);
	printf("Case #%d: ", Case);
	if (!n) {printf("INSOMNIA\n");return;}
	for(int i = 1;;i ++)
	{
		int cur = n * i;
		for(;cur;cur /= 10) Vis[cur % 10] = 1;
		bool ok = 1;
		for(int j = 0;j < 10;j ++)
			if (!Vis[j]) {ok = 0;break;}
		if (ok) 
		{
			printf("%d\n", n * i);
			return;
		}
	}
}

int main()
{
//	freopen("data.in","r",stdin),freopen("data.out","w",stdout);
	int T;
	scanf("%d", &T);
	for(int i = 1;i <= T;i ++) Work(i);
	return 0;
}
