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

int n, m, dem, res, way, dd[11], d[811][300];
string s[11];


void push(string s) {
    int t = 0;
    FOR(i, 0, sz(s) - 1) if (d[t][s[i]] == 0) {
        dem++;
        d[t][s[i]] = dem;
        t = dem;
    } else t = d[t][s[i]];
}

int Get(int u){
    dem = 0;
    FOR(i, 1, n) if (dd[i] == u) {
        push(s[i]);
    }
    FOR(i, 0, dem) FOR(j, 'A', 'Z') d[i][j] = 0;
   //memset(d, 0, sizeof d);
    return (dem + 1);
}

void check() {
    FOR(i, 1, m) {
        int ok = 1;
        FOR(j, 1, n) if (dd[j] == i) ok = 0;
        if (ok) return;
    }
    int sum = 0;
    FOR(i, 1, m) sum += Get(i);
    if (sum < res) return;
    if (sum > res) way = 0;
    way++;
    res = sum;
    //if (sum == 11) {FOR(i, 1, n) cout << dd[i] << ' ' ; cout << endl;}
}

void CAL(int i) {
    if (i == n + 1) check(); else{
        FOR(j, 1, m) {
            dd[i] = j;
            CAL(i + 1);
            dd[i] = 0;
        }
    }
}


void solve() {
    res = -1;
    way = 0;
    CAL(1);
    cout << res << ' ' << way << endl;
}


int main() {
     freopen("round2_D-small-attempt0.in","r",stdin);
     freopen("ans.out","w",stdout);
    int T;
    scanf("%d\n", &T);
    FOR(t, 1, T) {
        scanf("%d%d\n", &n, &m);
        FOR(i, 1, n) getline(cin, s[i]);
        //cout << n << ' ' << m << endl; FOR(i, 1, n) cout << s[i] << endl;
        cout << "Case #" << t << ": ";
        solve();
    }
     return 0;
}
