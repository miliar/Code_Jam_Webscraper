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

i64 n, p;

bool always(i64 a) {
	i64 b = a;
	i64 now = 0, z = 1LL << (n - 1);
	while (b > 0) {
		now += z;
		z /= 2;
		b = (b-1)/2;
	}
	return now < p;
}

bool can(i64 a) {
	i64 b = (1LL << n) - 1 - a;
	i64 now = 1LL << n, z = 1LL << (n - 1);
	while (b > 0) {
		now -= z;
		z /= 2;
		b = (b-1)/2;
	}
	return now <= p;
}

int main() {
	int CNT;
	cin >> CNT;
	FOR(cnt, 1, CNT) {
		cin >> n >> p;
		i64 ans1 = 0, ans2 = 0;

		FOR(i, 1, (1 << n) - 1) {
		//	printf("%d %d %d\n", i, always(i), can(i));
			if (always(i)) ans1 = i;
			if (can(i)) ans2 = i;
		}
		cout << "Case #" << cnt << ": " << ans1 << ' ' << ans2 << endl;;
	}
	
}
