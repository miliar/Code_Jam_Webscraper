#include<algorithm>
#include<bitset>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}

const int N = 1e6+5;
int n, p, q, r, s;
int t[N];
LL sum[N];

void solve(int tc) {
    scanf("%d %d %d %d %d", &n, &p, &q, &r, &s);
    REP(i, n) t[i] = ((LL(p)*i+q)%r+s);

    sum[0] = 0;
    REP(i, n) sum[i+1] = sum[i] + t[i];

    int a = 0, b = n, c;
    while (b - a > 1) {
        c = (a+b)/2;
        if (sum[c] <= sum[n] - sum[c]) {
            a = c;
        } else {
            b = c;
        }
    }
    --b;

    LL res = max(max(sum[a], sum[b]-sum[a]), sum[n]-sum[b]);
    while (b-a < n) {
        if (sum[a] > sum[n] - sum[b]) --a;
        else ++b;
        mini(res, max(max(sum[a], sum[b]-sum[a]), sum[n]-sum[b]));
    }
    printf("Case #%d: %.11Lf\n", tc, LD(sum[n] - res)/sum[n]);
}

int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);

    int t; scanf("%d", &t);
    REP(i, t) solve(i+1);
    
    return 0;
}

