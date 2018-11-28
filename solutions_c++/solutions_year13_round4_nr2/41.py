#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;


long long cal1(long long i, long long n, long long m) {
	//cout << i << ' ' << n << ' ' << m << endl;
	long long strong = i - 1, weak = n - i;
	if (strong > 0) {
		strong = (strong - 1) / 2;
		return (1ll << (m - 1)) + cal1(strong + 1, n >> 1, m - 1);
	} else {
	  return 0;
	}
}

long long cal2(long long i, long long n, long long m) {
	long long strong = i - 1, weak = n - i;
	if (weak > 0) {
		weak = (weak - 1) / 2;
		return cal2(n / 2 - weak, n >> 1, m - 1);
	} else {
	  return (1ll << m) - 1;
	}
}

int main() {
	
	freopen("B-Large.in", "r", stdin);
	freopen("B-L.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int V = 1; V <= T; ++V) {
	  long long ans1, ans2, n, p;
	  cin >> n >> p;
	  long long m = n;
	  n = (1ll << n);
	  --p;
	  long long l1 = 1, r1 = n, mid = 0;
	  while (r1 - l1 > 1) {
	    mid = (l1 + r1) / 2;
	    if (cal1(mid, n, m) <= p) l1 = mid; else r1 = mid;
		}
	  ans1 = (cal1(r1, n, m) <= p) ? r1 : l1;
	  l1 = 1, r1 = n, mid = 0;
	  while (r1 - l1 > 1) {
	    mid = (l1 + r1) / 2;
	    if (cal2(mid, n, m) <= p) l1 = mid; else r1 = mid;
		}
		ans2 = (cal2(r1, n, m) <= p) ? r1 : l1;
	  //cal
	  //if (ans1 < 0 || ans2 < 0) cout << m << ' ' << p << endl;
	  cout << "Case #" << V << ": " << ans1 - 1 << ' ' << ans2 - 1 << endl;
	}
	return 0;
}

