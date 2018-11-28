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
#define dprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}



void solve(int tc) {
    cout << "Case #" << tc << ": ";
    int n;
    cin >> n;
    vector<int> S(n);
    REP(i, n) {
        string s;
        cin >> s;
        REP(j, n) {
            if (s[j] == '1') S[i] += 1<<j;
        }
    }
    int M = 1ll<<(n*n);
    int R = 1ll<<n;
    int bst = n*n;
   // debugv(S);
    REP(msk, M) {
        VI T;
        int m = msk;
        REP(i, n) {
            T.PB(m % R);
            m /= R;
        }
        bool ok = true;
        REP(i,n) if ((T[i] & S[i]) != S[i]) ok = false;
        int tot = 0;
        REP(i, n) tot = tot | T[i];
        REP(i, n) REP(j, n) {
            if (T[i] != T[j] && (T[i] & T[j]) != 0) ok = false;
        }
        REP(i,n) {
            int c = __builtin_popcount(T[i]);
            REP(j,n) if (T[j] == T[i]) --c;
            if (c != 0) ok = false;
        }
        if (tot != R-1) ok = false;
        if (ok) {
       //     debugv(T);
            int sum = 0;
            REP(i,n) sum += __builtin_popcount(T[i] - S[i]);
            mini(bst, sum);
        }
    }
    cout << bst << endl;


}


int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);
    int T;
    cin >> T;
    REP(i,T) solve(i+1);


    return 0;
}

