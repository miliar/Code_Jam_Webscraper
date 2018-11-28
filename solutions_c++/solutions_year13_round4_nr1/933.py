#pragma comment(linker, "/STACK:33554432")

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <ctime>
#include <memory.h>

using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define ABS(n) ((n)<0 ? -(n) : (n))
#define SQR(a) (a)*(a)
#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define COPY(a,b) memcpy(a,b,sizeof (b));
#define SI(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define y1 yyyyy1
#define prev prevvvvv
#define LL long long
const double PI = 2*acos(0.0);
const double EPS = 1e-8;
const int INF = (1<<30)-1;

LL getP(LL N) {
    return (N*(N+1))/2;
}

LL getPenalty(LL L, LL N) {
    return getP(N) - getP(N-L);
}

LL fun (vector<LL>& v) {
    LL res = 0;
    REP(i,v.size()) while(v[i] > 0) {
        LL mn = v[i];
        int j = i;
        while (j+1 < v.size() && v[j+1] > 0) {
            ++j;
            mn = min<LL>(mn, v[j]);
        }
        res += getPenalty(j-i+1, v.size()+1) * mn;
        for (int k = i; k <= j; ++k) v[k] -= mn;

    }
    return res;
};

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

    int tc;
    cin >> tc;
    REP(ic,tc) {
        int n, m;
        cin >> n >> m;
        vector<LL> cums(n-1, 0);

        LL penalty = 0;

        REP(i,m) {
            int o, e, p;
            cin >> o >> e >> p;
            for (int j = o-1; j < e-1; ++j) cums[j] += p;
            penalty += getPenalty(e-o, n) * p;
        }
        cout << "Case #" << ic+1 << ": " << penalty - fun(cums) << endl;

    }

	return 0;
};