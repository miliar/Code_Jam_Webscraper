#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

long long b, n, sum[37], tsum[37];
double ans;

bool check(long long bar) {
	long long tmp = b;
	for (int i = 0; i < 37; ++i) {
	  if (sum[i] < bar) tmp -= bar - sum[i];
	}
	return tmp >= 0 && bar >= 0;
}

void trys(long long bar) {
	if (!check(bar)) return;
  double sums = 0;
	long long left = b;
	int cnt = 0;
  for (int i = 0; i < 37; ++i) {
  	if (sum[i] > bar) continue;
  	++cnt;
  	left -= bar - sum[i];
  	sums += bar - sum[i];
  }
  ans = max(ans, sums * 36 / cnt - b + left);
  for (int i = 36; i >= 0 && left > 0; --i) {
    if (sum[i] <= bar) {
			left -= 1;
      sums -= bar - sum[i];
			--cnt;
      ans = max(ans, sums * 36 / cnt - b + left);
		}
	}
}

int main() {
	
	freopen("A-Large.in", "r", stdin);
	freopen("A-Large.out", "w", stdout);
	
	int T = 0;
	scanf("%d", &T);
	for (int V = 1; V <= T; ++V) {
	  printf("Case #%d: ", V);
	  cin >> b >> n;
	  ans = 0;
	  memset(sum, 0, sizeof(sum));
		for (int i = 0; i < n; ++i) cin >> sum[i];
		sort(sum, sum + 37);
		for (int i = 0; i < 37; ++i) {
		  trys(sum[i]);
		  trys(sum[i] + 1);
		  if (sum[i] > 0) trys(sum[i] - 1);
		}
		long long l = 10000000, r = 0, mid;
		l *= l;
		while (l > r + 1) {
		  mid = (l + r) / 2;
		  if (check(mid)) {
		    trys(mid);
			  r = mid;
			} else {
			  l = mid;
			}
		}
		trys(l); trys(r); trys(l - 1); trys(l - 2);
		printf("%.10lf\n", ans);
	}
	return 0;
}

