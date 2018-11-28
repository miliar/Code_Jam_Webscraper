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

LL dp[101][10001][2], ar[101], gg[101], dd[101], tt[101], n, t1[101];
LL go(int c, int t, int f){
    if(c > n) return 0;
    LL &ret = dp[c][t][f];
    if(ret != -1) return ret;
    ret = 0;
    ret = go(c + 1, t + t1[c], f);
    if(dd[c] <= t + tt[c]) ret = max(ret, gg[c] + go(c + 1, t + tt[c] - dd[c], f));
    if(f == 0 && dd[c] == t + tt[c] + 1) ret = max(ret, gg[c] + go(c + 1, 0, 1));
    return ret;
}

main() {
    freopen("a.in", "r", stdin);
    freopen("b.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    LL a,b,c,d = 0,e,f = 0,g = 0,h = 0,x,y,z;
    cin >> a;
    FOR(ts, 1, a + 1){
        cin >> b >> c >> d;
        FOR(i, 1, d + 1){
            cin >> ar[i] >> gg[i];
            e = ar[i] % c;
            if(e == 0) e = c;
            dd[i] = (e + b - 1) / b;
            tt[i] = (ar[i] - e + c - 1) / c;
            t1[i] = (ar[i] + c - 1) / c;
        }
        memset(dp, -1, sizeof dp);
        n = d;
        cout << "Case #" << ts << ": " << go(1, 0, 0) << endl;
        cerr << "Case #" << ts << ": " << go(1, 0, 0) << endl;
    }
}
/*
1
25 54 4
45 321725
31 385094
31 23857
41 307841
*/
