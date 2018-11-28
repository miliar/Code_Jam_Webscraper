/*********************************************************************\
   |--\        ---       /\        |-----------| -----   /-------|    |
   |   \        |       /  \       |               |    /             |
   |    \       |      /    \      |               |   |              |
   |     \      |     /      \     |               |   |----|         |
   |      \     |    / ------ \    |-------|       |        |-----|   |
   |       \    |   /          \   |               |              |   |
   |        \   |  /            \  |               |              /   |
  ---        -------            ------           ----- |---------/    |
                                                                      |
    codeforces = nfssdq  ||  topcoder = nafis007                      |
    mail = nafis_sadique@yahoo.com || nfssdq@gmail.com                |
    IIT,Jahangirnagar University(41)                                  |
                                                                      |
**********************************************************************/

#include <bits/stdc++.h>

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

map < string, int > me, mf, mm;
vector < int > vc[22], vt;
vector < string > vp[22];
int ar[5005], id[5005], val[5005];
int main(){
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
    FOR(ts, 1, T+1){
        string s;
        int n; cin >> n;
        getline(cin, s);
        me.clear(); mf.clear(); mm.clear();
        vt.clear();
        REP(i, n){
            vc[i].clear(); vp[i].clear();
            getline(cin, s);
            istringstream is(s);
            string s1;
            while(is >> s1){
                vp[i].pb(s1);
                if(i == 0) me[s1] = 1;
                else if(i == 1) mf[s1] = 1;
                mm[s1] = 1;
            }
        }
        int cnt = 0;
        for(auto &v : mm){
            v.yy = ++cnt;
        }
        set0(ar); set0(id); set0(val);
        REP(i, n){
            REP(j, vp[i].size()){
                vc[i].pb( mm[ vp[i][j] ]);
                if(me[ vp[i][j] ]) val[ mm[vp[i][j]] ] |= 1;
                if(mf[ vp[i][j] ]) val[ mm[vp[i][j]] ] |= 2;
                if(i > 1) {
                    vt.pb(mm[ vp[i][j] ]);
                }

            }
        }

        int res = 100000000;
        cnt = 0;
        REP(i, 1<<(n-2)){
            cnt++;
            int sum = 0;
            for(int j = 2; j < n; j++){
                if(i & 1<<(j-2)){
                    REP(k, vc[j].size()){
                        if(id[ vc[j][k] ] != cnt) {
                            id[ vc[j][k] ] = cnt;
                            ar[ vc[j][k] ] = 0;
                        }
                        ar[ vc[j][k] ] |= 1;
                    }

                } else {
                    REP(k, vc[j].size()){
                        if(id[ vc[j][k] ] != cnt) {
                            id[ vc[j][k] ] = cnt;
                            ar[ vc[j][k] ] = 0;
                        }
                        ar[ vc[j][k] ] |= 2;
                    }
                }
            }
            REP(j, vt.size()){
                if(ar[vt[j]] == 4) continue;
                if((ar[vt[j]] | val[ vt[j] ]) == 3) sum++;
                ar[vt[j]] = 4;
            }
            res = min(res, sum);
        }
//        res = 0;
        REP(i, vc[0].size()){
            if(ar[vc[0][i]] == 4) continue;
            if(val[ vc[0][i] ] == 3) {
                res++;
//                cout << vp[0][i] << endl;
            }
            ar[ vc[0][i] ] = 4;
        }
        cout << "Case #" << ts << ": " << res << endl;
        cerr << "Case #" << ts << ": " << res << endl;
    }
}
