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
template<class T> void fmax(T &a, const T &b) { if (a < b) a = b; }
template<class T> void fmin(T &a, const T &b) { if (a > b) a = b; }
template<class T> T sqr(const T &a) { return a * a; }

int n, m;
i64 ans;
vector<pair<i64, i64> >  a;

i64 MOD = 1000002013;

i64 g(i64 k) {
	if (!k) return 0;
	return (n + n - k + 1) * k / 2 % MOD;
}


int main() {
	int CNT;
	cin >> CNT;
	FOR(cnt, 1, CNT) {
		cin >> n >> m;
		a.clear();
		i64 ans0 = 0;
		FOR(i, 1, m) {
			i64 x, b, c;
			cin >> x >> b >> c;
			a.PB(MP(x, -c));
			a.PB(MP(b, c));
			ans0 += g(b - x) * c % MOD;
		}
	//	cout << "ANS0 " << ans0 << endl;
		sort(a.begin(), a.end());
		ans = 0;
		priority_queue<pair<i64, i64> > Q;
		rep(w, (int) a.size()) {
			i64 t =-a[w].second;
			i64 x = a[w].first;
		//	cout << x << ' ' << t << endl;
			if (t > 0) {
				Q.push(make_pair( x, t));
			}
			else {
				t = -t;
				while (t > 0) {
					pair<int, int> a = Q.top();
					Q.pop();
					i64 X = a.first;
					i64 y = a.second;
//cout << "POP"  << X  << ' ' << y << endl;
					i64 q = min(y, t);
					y -= q;
					t -= q;
					ans += g(x - X) * q % MOD;
					if (y > 0) Q.push(make_pair(X,  y));
				//cout << "ANS = " << ans << endl;
				}
			}
		}
		i64 www = (ans0 - ans)% MOD + MOD * 10;
		www %= MOD;
		cout << "Case #" << cnt << ": " << www << endl;
	}
	
}
