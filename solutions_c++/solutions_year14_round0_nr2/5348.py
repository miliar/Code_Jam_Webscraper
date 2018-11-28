#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
using namespace std;
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define REP(i,a,b) for(int i=a; i>=b; i--)
#define FORAD(i,u) for(int i=0; i < (int)u.size(),i++)
#define BUG(x) cout << x << endl
#define ll long long
#define fi first
#define sd second
#define pb push_back
#define two(i) 1 << i
#define sz(x) (int)x.size()
#define e 1e-12
#define bit(s,i) ((s >> (i-1)) & 1)
#define Nmax 100100
const double pi = acos(-1);
typedef vector<int> vi ;
typedef pair<int,int> pii ;

double C, F, X, res, Count, value;

void solve() {
    cin >> C >> F >> X;
    value = 2;
    res = 1000000000;
    Count = 0;
    FOR(i, 1, 10000000) {
        if (Count > res) break;
        res = min(res, Count + X/value);
        Count += C/value;
        value += F;
    }
    printf("%0.7f\n", res);
}

int main() {
     freopen("in.inp","r",stdin);
     freopen("ans.out","w",stdout);
     int test;
     scanf("%d", &test);
     FOR(t, 1, test) {
            printf("Case #%d: ", t);
            solve();
     }
     return 0;
}
