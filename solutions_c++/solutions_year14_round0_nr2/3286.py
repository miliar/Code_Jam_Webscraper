#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <queue>
#include <map>
#include <vector>
#include <cmath>
#include <set>
#include <utility>

#define eps 1e-9
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define sz(x) (int)(x).size()
#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define ms(x,i) memset((x),(i),sizeof((x)))
#define debug(x) if(DEBUG) cout << x << endl
#define DEBUG 1

using namespace std;

typedef long long ll;
typedef pair<int,int> pt;
typedef pair<pt,int> ppt;
const int nmax = 1000013;
int t;
double C, F, X, ans, rs;
double income;
void turn() {
    rs += C/income;
    income += F;
    ans = min(ans,X/income + rs);
}
void solve(int test) {
    scanf("%lf%lf%lf", &C, &F, &X);
    income = 2.0;
    ans = X/2.0;
    rs = 0.0;
    FOR(number,1,100000) {
        turn();
        if(rs > ans) break;
    }
    printf("Case #%d: %.9lf\n", test, ans);
}
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d", &t);
    FOR(i,1,t) {
        solve(i);
    }
    return 0;
}
