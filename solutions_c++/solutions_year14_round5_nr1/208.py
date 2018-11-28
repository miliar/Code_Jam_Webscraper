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

LL ar[1000001];
LL sum[1000001];
main() {
    freopen("a.in", "r", stdin);
    freopen("b.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    LL a,b,c,d = 0,e,f = 0,g = 0,h = 0,x,y,z;
    cin >> a;
    FOR(ts, 1, a + 1){
        cin >> b >> c >> d >> e >> f;
        set0(ar); set0(sum);
        REP(i, b){
            ar[i + 1] = ((i * c + d) % e + f);
            sum[i + 1] = sum[i] + ar[i + 1];
        }
        f = 0;
        d = 1;
        for(int i = 1; i <= b; i++){
            while(d <= b){
                x = sum[i - 1], y = sum[d] - sum[i - 1], z = sum[b] - sum[d];
                if((y < x || y < z) && d < b)d++;
                else break;
            }
            g = max(x, max(y, z));
            h = x + y + z - g;
            f = max(f, h);
        }
        for(int i = 1; i <= b; i++){
            d = lower_bound(sum + 1, sum + b + 1, sum[i]*2) - sum;
            d--;
            if(d <= i) continue;
            x = sum[i]; y = sum[d] - sum[i], z = sum[b] - sum[d];
            if(x >= y && x >= z) f = max(y + z, f);
        }
        reverse(ar + 1, ar + b + 1);
        FOR(i, 1, b + 1) sum[i] = sum[i - 1] + ar[i];
        for(int i = 1; i <= b; i++){
            d = lower_bound(sum + 1, sum + b + 1, sum[i]*2) - sum;
            d--;
            if(d <= i) continue;
            x = sum[i]; y = sum[d] - sum[i], z = sum[b] - sum[d];
            if(x >= y && x >= z) f = max(y + z, f);
        }
        double p = (double) f / (double) (sum[b]);
        cout << "Case #" << ts << ": " << fixed << setprecision(10) << p << endl;
        cerr << "Case #" << ts << ": " << fixed << setprecision(10) << p << endl;
    }
}


