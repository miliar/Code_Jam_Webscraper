#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int oo = 0x3f3f3f3f;
typedef long long ll;
int n, cnt;
ll ans;
int ha[20];

inline bool cal(ll x)
{
	ans = x;
	int now;
	while(x)
	{
		now = x % 10;
		x /= 10;
		if(ha[now]) continue;
		ha[now] = 1;
		cnt ++;
		if(cnt >= 10) return 1;
	}
	return 0;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int T;
	int k = 0;
	scanf("%d",&T);
	while(T--)
	{
		cnt = 0;
		memset(ha, 0 , sizeof(ha));
		scanf("%d",&n);
		if(!n) { printf("Case #%d: INSOMNIA\n",++k); continue;}
		ll num = 1;
		while(!cal((ll)n * num++));
		printf("Case #%d: %lld\n",++k, ans);
	}

	return 0;
}
