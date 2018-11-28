#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;
typedef long long int64;
typedef pair<int, int> PII;
const int MOD = 1000000007;
const double EPSILON = 1e-10;

#define FORU(i, a, b) for (int i = (a); i <= (b); ++i)
#define FORD(i, a, b) for (int i = (a); i >= (b); --i)
#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define SIZE(A) ((int) A.size())
#define PB(X) push_back(X)
#define MP(A, B) make_pair(A, B)

template<class T> inline T tmin(T a, T b) {return (a < b) ? a : b;}
template<class T> inline T tmax(T a, T b) {return (a > b) ? a : b;}
template<class T> inline T tabs(T a) {return (a > 0) ? a : -a;}
template<class T> T gcd(T a, T b) {if (b == 0) return a; return gcd(b, a % b);}

int main(int argc, char const *argv[])
{	
	ios_base::sync_with_stdio(false);
	int ntest, N, X;
	int a[10001], cnt[701];
	cin >> ntest;
	FORU(t, 1, ntest) {
		memset(cnt, 0, sizeof(cnt));
		cin >> N >> X;
		REPU(i, 0, N) {
			cin >> a[i];
			cnt[a[i]]++;
		}
		cnt[0] = 1000005;
		sort(a, a + N);
		int ans = 0;
		FORD(i, N-1, 0) {
			if (cnt[a[i]] == 0) continue;
			cnt[a[i]]--;
			FORD(j, X - a[i], 0) {
				if (cnt[j] > 0) {
					cnt[j]--;
					ans++;
					break;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}