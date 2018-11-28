#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
using namespace std;

#define rep(i,n) for(int i = 0; i < (int)n; i++)
#define FOR(i,n,m) for(int i = (int)n; i <= (int)m; i++)
#define FOD(i,n,m) for(int i = (int)n; i >= (int)m; i--)
#define EACH(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

typedef long long i64;
typedef pair<int, int> PI;

#define sz(v) ((i64)(v).size())
#define all(v) (v).begin(),(v).end()
#define bit(n) (1LL<<(i64)(n))

#define PB push_back
#define MP make_pair
#define X first
#define Y second

const int INF = 1e9;
const double Pi = acos(-1.0);
const double eps = 1e-5;

template<class T> void fmax(T &a, const T &b) { if (a < b) a = b; }
template<class T> void fmin(T &a, const T &b) { if (a > b) a = b; }
template<class T> T sqr(const T &a) { return a * a; }

const int N = 10010;

int n, m, ans;
string s;
double f[1050 * 1050];

int main() {
	int CNT;
	cin >> CNT;
	FOR(cnt, 1, CNT) {
		cin >> s;
		n = s.length();
		m = 1 << n;
		int init = 0;
		rep(i, n) if (s[i] == 'X') init |= 1 << i;
		double ans = 0;
		memset(f, 0, sizeof(f));
		f[init] = 1.0;
		FOR(msk, init, m - 2) {
			double p = f[msk] / n;
			int l = 0;
			while (msk & (1 << l)) l++;
			FOD(j, n - 1, 0) {
				if (msk & (1 << j)) l++;
				else l = 0;
				ans += p * (n - l);
				int x = j + l;
				if (x >= n) x -= n;
				f[msk | (1 << x)] += p;
			}
		}
		printf("Case #%d: %.15f\n", cnt, ans);
	//	cout << "Case #" << cnt << ": " << ans << endl;
	}
}
