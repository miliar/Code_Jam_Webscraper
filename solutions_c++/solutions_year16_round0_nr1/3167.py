#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#define maxn 20
typedef long long ll;
using namespace std;
int T, n, cnt;
ll x;
bool occ[maxn];
void split(ll x)
{
	ll t;
	while (x){
		t = x % 10ll; x /= 10ll;
		if (! occ[t]) ++ cnt, occ[t] = 1;
	}
}
void solve(int cas)
{
	scanf("%d", &n); x = 0;
	printf("Case #%d: ", cas);
	if (n == 0){
		puts("INSOMNIA");
		return;
	}
	memset(occ, 0, sizeof(occ)); cnt = 0;
	for (int i = 1; i <= 1000; ++ i){
		x += n; split(x);
		if (cnt == 10) break;
	}
	printf("%lld\n", x);
}
int main()
{
	scanf("%d", &T);
	for (int i = 1; i <= T; ++ i) solve(i);
	return 0;
}


