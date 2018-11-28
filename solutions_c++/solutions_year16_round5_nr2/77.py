#include<cstdio>
#include<cstring>
#include<cassert>
#include<vector>
#include<list>
#include<queue>
#include<map>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<fstream>
#include<typeinfo>
#include<locale>
#include<iterator>
#include<valarray>
#include<complex>
#include<climits>

using namespace std;

#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define LL         long long
#define inf        INT_MAX/3
#define mod        1000000007ll
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     ((A).begin(), (A).end())
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)

//cout << fixed << setprecision(20) << p << endl;

template <class T> inline T bigmod(T p,T e,T M){
    LL ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}


vector < int > vc[101];
int pre[101];
vector < int > vp[30];


int TF[1001][27];
string pat;
void computeFA(int M){
    int lps = 0;

    for(int i = 0; i < 26; i++) TF[0][i] = 0;
    TF[0][pat[0] - 'A'] = 1;

    for(int i = 1; i < M; i++){
        for(int j = 0; j < 26; j++) TF[i][j] = TF[lps][j];
        TF[i][pat[i] - 'A'] = i + 1;
        if(i < M) lps = TF[lps][pat[i] - 'A'];
    }
}

vector < int > dfs2(int c){
    vector < int > cur;
    REP(i, vc[c].size()){
        vector < int > tmp = dfs2(vc[c][i]);
        vector < int > vt = cur;
        cur.clear();
        int s1 = 0, s2 = 0;
        REP(j, vt.size() + tmp.size()){
            if(s1 == tmp.size()) cur.pb(vt[s2++]);
            else if(s2 == vt.size()) cur.pb(tmp[s1++]);
            else {
                int p1 = (vt.size() - s2), p2 = (tmp.size() - s1);
                if(rand() % (p1+p2) < p1) cur.pb(vt[s2++]);
                else cur.pb(tmp[s1++]);
            }
        }
    }
    vector < int > vt = cur;
    cur.clear();
    cur.pb(c);
    REP(i, vt.size()) cur.pb(vt[i]);
    return cur;
}

int ar[111];

int main() {
    srand(79);
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);

    int T; cin >> T;
    FOR(ts, 1, T+1){
        int n; cin >> n;
        REP(i, n+1){
            vc[i].clear();
        }
//        REP(i, 26) vp[i].clear();
        REP(i, n){
            cin >> pre[i+1];
            vc[pre[i+1]].pb(i+1);
        }
        string S; cin >> S;
        S = "#" + S;
//        FOR(i, 1, S.size()) vp[S[i]-'a'].pb(i);

//        set0(on);
//        double tot = dfs(0);
        cout << "Case #" << ts << ": ";
        int q; cin >> q;
        REP(i, q){
            string s; cin >> s;
            pat = s;
            computeFA(pat.size());

            double cc = 0;
            set < int > ss;
            REP(j, 10000){
                vector < int > v = dfs2(0);

                int st = 0;
                FOR(k, 1, n+1){
//                    cout << S[v[k]];
                    st = TF[st][ S[v[k]]-'A' ];
                    if(st == s.size()){
                        cc++;
                        break;
                    }
                }
//                cout << endl;
            }
            if(i) cout << " ";
            cout << fixed << setprecision(10) << cc/10000.0;
        }
        cout << endl;
        cerr << ts << endl;
    }
}
