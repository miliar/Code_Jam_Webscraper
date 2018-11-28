
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <complex>

using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }


ll A, B;

vector <ll> result;

bool isprime(ll num) {
	vector<int> x;
	ll tmp = num;
	while (tmp) { x.push_back(tmp % 10); tmp /= 10; }
	rep (i, (int)x.size()) if (x[i] != x[(int)x.size() - 1 - i]) return false;
	return true;
}

void preinit() {
	fo (i, 1, 10000) {
		rep (g, 2) {
			vector<int> x;
			ll tmp = i;
			while (tmp) { x.push_back(tmp % 10); tmp /= 10; }
			if (x[0] == 0) continue;
			int s = x.size() - g;
			for (int j = s - 1; j >= 0; j--) x.push_back(x[j]);
			ll num = 0;
			for (int j = x.size() - 1; j >= 0; j --)
				num = num * 10 + x[j];
			if (isprime(num*num)) {
				result.push_back(num*num);
			}
		}
	}

}

void solve() {
	scanf("%lld%lld", &A, &B);
	int res = 0;
	for (int i = 0; i < (int)result.size(); i++)
			if (result[i] >= A && result[i] <= B) res++;
	printf("%d", res);
}

int main(int argc, char ** argv) {
	preinit();
	//  freopen("../1.in","r",stdin); 
	//  freopen("../2.in","r",stdin); 
	//  freopen("../3.in","r",stdin); 
	//  freopen("../A-small.in","r",stdin); freopen("../A-small.out","w",stdout);
	//  freopen("../A-small-attempt0.in","r",stdin);freopen("../A-small-attempt0.out","w",stdout);
	//  freopen("../A-small-attempt1.in","r",stdin);freopen("../A-small-attempt1.out","w",stdout);
	//  freopen("../A-small-attempt2.in","r",stdin);freopen("../A-small-attempt2.out","w",stdout);
	//  freopen("../A-large.in","r",stdin); freopen("../A-large.out","w",stdout)

	cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
	int t;
	scanf("%d", &t);
	fo (i, 1, t) {
		printf("Case #%d: ", i);
		solve();
		printf("\n");
		fflush(stdout);
		cerr.flush();
	}
	return 0;
}


