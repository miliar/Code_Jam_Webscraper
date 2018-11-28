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
#define PI         2.0*acos(0.0)
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


LL dp[1011][1011], ar[1011], pre[1011], nxt[1011];
LL tmp[1011], pos[1011], n;
LL go(int c, int p){
    if(c > n) return 0;
    LL &ret = dp[c][p];
    if(ret != -1) return ret;
    ret = inf;
    ret = min(ret, pre[pos[c]] + go(c + 1, p + 1));
    ret = min(ret, nxt[pos[c]] + go(c + 1, p));
    return ret;
}
main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    LL a,b,c,d = 0,e = 0,f = 0,g,h = 0,x = 0,y,z;
    cin >> a;
    FOR(ts, 1, a + 1){
        cout << "Case #" << ts << ": ";
        cerr << "Case #" << ts << ": ";
        memset(dp, -1, sizeof dp);
        cin >> b;
        set0(pre); set0(nxt);
        FOR(i, 1, b + 1) cin >> ar[i];
        for(int i = 1; i <= b; i++){
            tmp[i] = ar[i];
            for(int j = i - 1; j >= 1; j--) if(ar[j] > ar[i]) pre[i]++;
            for(int j = i + 1; j <= b; j++) if(ar[j] > ar[i]) nxt[i]++;
        }
        sort(tmp + 1, tmp + b + 1);
        for(int i = 1; i <= b; i++){
            for(int j = 1; j <= b; j++) if(ar[j] == tmp[i]) pos[i] = j;
        }
        n = b;
        d = go(1, 0);
        cout << d << endl;
        cerr << d << endl;
     }
}

