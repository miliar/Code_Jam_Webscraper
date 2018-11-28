#include "iostream"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "queue"
#include "stack"
#include "cmath"
#include "utility"
#include "map"
#include "set"
#include "vector"
#include "list"
#include "string"
#include "cstdlib"
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define st first
#define nd second
#define exp 1e-8
const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
int t, num;
ll n, ans;
std::map<int, bool> mp;
void Magic(ll x)
{
	while(x != 0) {
		ll y = x % 10;
		if(!mp[y]) {
			mp[y] = true;
			num++;
		}
		x /= 10;
	}
}
int main(int argc, char const *argv[])
{
	freopen("A-large.in", "r+", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for(int cas = 1; cas <= t; ++cas) {
		mp.clear();
		ans = num = 0;
		scanf("%lld", &n);
		if(n == 0) {
			printf("Case #%d: INSOMNIA\n", cas);
			continue;
		}
		for(int i = 1; i <= 1e6; ++i) {
			ll x = 1ll * i * n;
			Magic(x);
			if(num == 10) {
				ans = x;
				break;
			}
		}
		printf("Case #%d: %lld\n", cas, ans);
	}
	return 0;
}