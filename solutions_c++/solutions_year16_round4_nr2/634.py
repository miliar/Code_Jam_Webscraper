#include <queue>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <cstdio>
using namespace std;
#define V vector
#define tD typedef
tD long long ll;
tD V<int> vi;
tD V<vi> vii;
tD V<ll> vll;
tD V<string> vs;
tD V<double> vd;
tD long double ld;
tD pair<int, int> pii;
#define prr make_pair
#define fr(x,y) for(int x=0;x<(y); ++x)
#define fi(n) fr(i,n)
#define fj(n) fr(j,n)
#define fk(n) fr(k,n)
#define pb push_back
#define sz size()
#define DEBUG 0

vector<double> prob;

double TieProb(const vd &cur) {
    vd distrib(cur.sz + 1, 0);
    distrib[0] = 1.0;
    fi(cur.sz) {
        for (int j = distrib.sz - 1; j >= 0; j--) {
            distrib[j] = distrib[j] * (1.0 - cur[i]) + (j ? distrib[j-1] * cur[i] : 0.0);
        }
    }
    //fi(distrib.sz) {
    //    printf("%.4lf ", distrib[i]);
    //}
    //printf("\n");
    return distrib[cur.sz / 2];
}

int main() {
    int T; cin >> T;
    for (int qw = 1 ; qw <= T; qw++) {
        int N, K; cin >> N >> K;
        prob.clear();
        fi(N) { double a; cin >> a; prob.pb(a); }
        sort(prob.begin(), prob.end());
        double best = 0.0;
        fj(K+1) {
            vd cur;
            fi(j) {
                cur.pb(prob[i]);
            }
            for (int i = prob.sz - 1; i >= int(prob.sz) - (K - j); i--) {
                cur.pb(prob[i]);
            }
            if (TieProb(cur) > best) {
                best = TieProb(cur);
            }
        }
        printf("Case #%d: ", qw);
        printf("%.8lf\n", best);
    }
}
