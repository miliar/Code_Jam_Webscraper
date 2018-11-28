#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define EPS 1e-10
#define INF 1000000000000
#define mp make_pair
#define pb push_back

typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;
typedef long long ll;

bool is_asleep(vector<bool> digits) {
	for (int d = 0; d < 10; d++) {
		if (!digits[d]) return false;
	}
	return true;
}

void update_digits(vector<bool> &digits, ll num) {
	while (num > 0) {
		int d = num % 10;
		digits[d] = true;
		num /= 10;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int N;
		scanf("%d", &N);
		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		vector<bool> digits(10, false);
		ll ans = 0;
		for (ll i = 1; i < INF; i++) {
			ll Ni = N * i;
			update_digits(digits, Ni);
			if (is_asleep(digits)) {
				ans = Ni;
				break;
			}
		}
		printf("Case #%d: %lld\n", t, ans);
	}
}

