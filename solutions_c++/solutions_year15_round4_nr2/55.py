#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;

typedef long long LL;
typedef vector<int> VI;

#define REP(i,n) for(int i=0, i##_len=(n); i<i##_len; ++i)
#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(),i##_end=(c).end();i!=i##_end;++i)
#define eprintf(s...) fprintf(stderr, s)

template<class T> inline void amin(T &a, const T &b) { if (b<a) a=b; }
template<class T> inline void amax(T &a, const T &b) { if (a<b) a=b; }

typedef long double Double;
const Double EPS = 1e-12;
const Double INF = 1e16;

int T;
int N;
Double V, X;
pair<Double, Double> P[111];


bool ok(Double M) {
    // cool
    {
	Double vol = 0, tem = 0;
	REP (i, N) {
	    Double v1 = min(V - vol, P[i].second * M);
	    Double vv = vol + v1;
	    if (v1 == V - vol) vv = V;
	    else vv = vol + v1;
	    tem = (vol * tem) / vv + (v1 * P[i].first) / vv;
	    vol = vv;
	}
	if (vol < V || tem-EPS > X) return false;
    }
    // hot
    {
	Double vol = 0, tem = 0;
	REP (i_, N) {
	    int i = N-1-i_;
	    Double v1 = min(V - vol, P[i].second * M);
	    Double vv = vol + v1;
	    if (v1 == V - vol) vv = V;
	    else vv = vol + v1;
	    tem = (vol * tem) / vv + (v1 * P[i].first) / vv;
	    vol = vv;
	}
	if (vol < V || tem < X-EPS) return false;
    }
    return true;
}

int main() {
    int T;
    scanf("%d", &T);
    
    for (int tc=1; tc<=T; tc++) {
	double V_, X_; 
	scanf("%d%lf%lf", &N, &V_, &X_);
	V = V_; X = X_;
	REP (i, N) {
	    double R, C;
	    scanf("%lf%lf", &R, &C);
	    P[i] = make_pair(C, R);
	}

	sort(P, P+N);

	printf("Case #%d: ", tc);

	if (!ok(INF)) {
	    puts("IMPOSSIBLE");
	} else {
	    Double lo = 0, hi = INF;
	    REP (k, 5000) {
		Double m = (lo + hi) / 2;
		if (ok(m)) hi = m;
		else lo = m;
	    }
	    printf("%.12Lf\n", (lo + hi) / 2);
	}
    }
    return 0;
}
