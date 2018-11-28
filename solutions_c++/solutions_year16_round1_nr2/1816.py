#include <bits/stdc++.h>
using namespace std;

#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define FOREACH(it, a) for (auto it = a.begin(); it != a.end(); ++it)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())

typedef long long ll;
const int MOD = 1000000007;

template<class T, class U> inline T tmin(T a, U b) { return (a < b) ? a : b; }
template<class T, class U> inline T tmax(T a, U b) { return (a > b) ? a : b; }
template<class T, class U> inline void amax(T &a, U b) { if (b > a) a = b; }
template<class T, class U> inline void amin(T &a, U b) { if (b < a) a = b; }
template<class T> inline T tabs(T a) { return (a > 0) ? a : -a; }
template<class T> T gcd(T a, T b) { while (b != 0) { T c = a; a = b; b = c % b; } return a; }

const int N = 2555;
int cnt[N];

int main(int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
	
	int nTest, n, a;

	cin >> nTest;
	REPU(it, 1, nTest + 1) {
		cin >> n;
		vector<int> x;
		MEM(cnt, 0);
		REPU(i, 1, n + n) {
			REPU(j, 0, n) {
				cin >> a;
				x.push_back(a);
				cnt[a]++;
			}
		}
		sort(ALL(x)); UNIQUE(x);
		vector<int> ans;
		REPU(i, 0, x.size()) {
			if (cnt[x[i]] & 1) ans.push_back(x[i]);
		}
		printf("Case #%d: ", it);
		REPU(i, 0, n) printf("%d%c", ans[i], " \n"[i == n - 1]);
	}
	
	return 0;
}
