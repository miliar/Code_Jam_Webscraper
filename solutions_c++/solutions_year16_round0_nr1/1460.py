#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;

const int maxn = 1E6 + 10;
typedef int LL;

LL n,now,a[maxn],tot;
bool bo[10];

void cal(LL x)
{
	for (; x; x /= 10) {
		int y = x % 10;
		if (!bo[y]) bo[y] = 1,--tot;
	}
}

int main()
{
	#ifdef YZY
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	
	cin >> n;
	for (int i = 1; i <= n; i++) {
		scanf("%d",&now);
		if (!now) {printf("Case #%d: INSOMNIA\n",i); continue;}
		tot = 10; memset(bo,0,sizeof(bo));
		for (LL j = 1; j <= 100; j++) { 
			LL x = now*j;
			cal(x); 
			if (!tot) {printf("Case #%d: %d\n",i,x); break;}
		}
	}
	return 0;
}

