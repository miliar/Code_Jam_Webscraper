#include<iostream>
#include<iomanip>
#include<map>
#include<unordered_map>
#include<set>
#include<unordered_set>
#include<vector>
#include<array>
#include<string>
#include<stack>
#include<queue>
#include<algorithm>
#include<cassert>
#include<functional>
#include<random>
#include<complex>
#include<bitset>
#include<chrono>
//#include<boost/multiprecision/cpp_int.hpp>
#define int int64_t
#define uint uint64_t
#define REP(i, a, b) for (int64_t i = (int64_t)(a); i < (int64_t)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define SZ(X) ((int64_t)((X).size()))
#define ITR(x, a) for (auto x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define Min(x) *min_element(ALL(x))
#define Max(x) *max_element(ALL(x))
#define Unique(L) (L.erase(unique(ALL(L)), L.end()))
#define intmax (std::numeric_limits<int64_t>::max() / 4)
#define doublemax (std::numeric_limits<double>::max() / 4)
using namespace std;
//typedef boost::multiprecision::cpp_int bigint;
const double EPS = 1e-9;
const double PI = acos(-1.0);



signed main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	rep(tt, T) {
		string S;
		int K;
		cin >> S >> K;

		int L = S.size();
		vector<int>imos(L + 1, 0);
		int flip = 0, ans = 0;
		rep(i, L) {
			flip -= imos[i];
			int x = flip + (S[i] == '+' ? 0 : 1);
			if (x % 2) {
				if (L - K < i) {
					ans = -1;
					break;
				}
				flip++;
				ans++;
				imos[i + K]++;
			}
		}
		if (ans == -1)cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << tt + 1 << ": " << ans << endl;
	}



	return 0;
}