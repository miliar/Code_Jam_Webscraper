#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <map>
#include <iostream>
using namespace std;

template <class T>
inline void PT(T x) {
    if (x < 0) {
        putchar('-');

        x = -x;
    }
    if (x > 9) PT(x / 10);
    putchar(x % 10 + '0');
}

typedef __int128 ll;
void print(int num) {
	printf("1");
	for(int i = 29; i >= 0; i --) 
		printf("%d", (num >> i) & 1); 
	printf("1");
}

//Miller Rabin素数测试
const int Times = 7; //错误概率为1/4^Times
ll mulMod(ll a, ll b, ll m) {
  ll r = 0;
  for (a %= m, b %= m; b; b >>= 1) { if (b & 1) { r = (r + a) % m; } a = (a << 1) % m; }
  return r;
}
ll powMod(ll a, ll b, ll m) {
  ll r = 1;
  for (a %= m; b; b >>= 1) { if (b & 1) { r = mulMod(r, a, m); } a = mulMod(a, a, m); }
  return r;
}
bool Miller_Rabin(ll n) {
  if (n == 2) { return true; }
  if (n < 2 || (n & 1) == 0) { return false; }
  ll m = n - 1; int k = 0;
  while ((m & 1) == 0) { k++; m >>= 1; }
  for (int i = 0; i < Times; i++) {
    ll a = rand() % (n - 1) + 1, x = powMod(a, m, n), y = 0;
    for (int j = 0; j < k; j++) {
      y = mulMod(x, x, n);
      if (y == 1 && x != 1 && x != n - 1) { return false; }
      x = y;
    }
    if (y != 1) { return false; }
  }
  return true;
}

int a[55];
ll go(int base) {
	ll ans = 0;
	for(int i = 31; i >= 0; i --)
		ans = ans * base + a[i];
	return ans;
}
bool ok(int num) {
	a[0] = a[31] = 1;
	for(int i = 0; i < 30; i ++) a[i + 1] = (num >> i) & 1;
	for(int i = 2; i <= 10; i ++)
		if(Miller_Rabin(go(i))) return false;
	return true;
}
ll ans[13];
int main() {
	//freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int lim = 1 << 30;
	int nd = 500;
	printf("Case #1:\n");
	for(int num = 0; num < lim && nd; num ++) {
		if(ok(num)) {
			bool flag = 1;
			for(int i = 2; i <= 10; i ++) {
				ll tmp = go(i);
				for(ll j = 2; j * j <= tmp; j ++) {
					if(j == 1e6) {
						flag = false;
						break;
					}
					if(tmp % j == 0) {
						ans[i] = j;
						break;
					}
				}
			}
			if(flag) {
				print(num);
				for(int i = 2; i <= 10; i ++) {
					printf(" ");
					PT(ans[i]);
				}
				puts("");
				nd --;
			}
		}
	}
}
