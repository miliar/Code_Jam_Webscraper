#include "cstdio"
#include "iostream"
#include "vector"
#include "algorithm"
#include "cstring"
#include "set"
#include "map"
#define runtime() ((double)clock() / CLOCKS_PER_SEC)
#define rep(i, n) for(int i=0; i<n; i++)
#define repp(i, a, b) for(int i=a; i<a+b; i++)
using namespace std;
inline int getint(){
  char c = getchar();
  for(;c<'0'||c>'9';) c = getchar();
  int x = 0;
  for(;c>='0' && c<='9'; c = getchar()) x*=10, x+=c-'0';
  return x;
}
const int N = 1000 + 10;

set<int> vis;
int a[N];
int n, Cases;
int ans;

int main()
{
	cin >> Cases;
	for (int t = 1; t <= Cases; ++t) {
		ans = 0;
		vis.clear();
		cin >> n;
		rep(i,n) a[i] = getint();
		int l = -1, r = n;
		rep(i,n) {
			int k = -1;
			rep(j,n)
				if (! vis.count(a[j]) && (k == -1 || a[j] < a[k])) k = j;
			vis.insert(a[k]);
			int Left, Right;
			for (Left = k - 1; Left >= 0; --Left)
				if (Left <= l && a[Left] < a[k]) break;
			for (Right = k + 1; Right < n; ++Right)
				if (Right >= r && a[Right] < a[k]) break;
			if (k - Left - 1 < Right - k - 1) {
				for (int j = k; j > Left + 1; --j) swap(a[j], a[j - 1]); ans += k - Left - 1; ++l;
			}
			else {
				for (int j = k; j < Right - 1; ++j) swap(a[j], a[j + 1]); ans += Right - k - 1; --r;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}