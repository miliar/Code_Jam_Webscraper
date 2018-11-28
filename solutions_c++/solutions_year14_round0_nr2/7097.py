//mohamed magdi
//moh_magdi@acm.org
#include <bits/stdc++.h>

#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#endif

#define all(v)          v.begin(),v.end()
#define allr(v)         v.rbegin(),v.rend()
#define rep(i,m)        for(int i=0;i<(int)m;i++)
#define REP(i,k,m)      for(int i=k;i<(int)m;i++)
#define mem(a,b)        memset(a,b,sizeof(a))
#define mp              make_pair
#define pb              push_back
#define X real()
#define Y imag()

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;
typedef complex<long double> point;

int diri[] = { -1, 0, 1, 0, -1, 1, 1, -1 };
int dirj[] = { 0, 1, 0, -1, 1, 1, -1, -1 };

int compare(double d1, double d2) {
	if (fabs(d1 - d2) < 1e-9)
		return 0;
	if (d1 < d2)
		return -1;
	return 1;
}
#define OO ((int)1e9)
#define MAX 1000001
#define MOD 1000000009

#define SMALL
#define LARGE

int T;

int main() {
	std::ios_base::sync_with_stdio(false);
	freopen("1.in", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt2.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		double rate = 2.0, f, c, x, curC = 0, t = 0;
		scanf("%lf%lf%lf", &c, &f, &x);

		double bestT = x / rate;
		for (int i = 0; i <= 2*x; i++) {
			double tToWin = x / rate;
			if (compare(bestT, t + tToWin) > 0)
				bestT = min(bestT, t + tToWin);
			double tToBuy = (c - curC) / rate;
			curC = 0;
			t += tToBuy;
			rate += f;
		}
		printf("%.7lf\n", bestT);
	}
	return 0;
}
//end

