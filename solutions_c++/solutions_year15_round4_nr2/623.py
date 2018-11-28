#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstring>
#include <fstream>
#include <ctime>
#include <iomanip>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOD(i,a,b) for(int i=a;i>b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define debug cout << "YES" << endl
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)

using namespace std;

typedef pair<int, int>II;
typedef pair<int,II>PII;
template<class T> T gcd(T a, T b) {T r; while(b!=0) {r=a%b;a=b;b=r;} return a;}
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }

const long double PI = 2*acos(0.0);
const long double eps = 1e-12;
const int infi = 1e9;
const LL Linfi = (LL) 1e18;
const LL MOD = 1000000007;
const int c1 = 31;
const int c2 = 37;
#define maxn 1000005

int n;
long double V, X, R[105], C[105];

int cmp(long double a, long double b){
    if(abs(a-b) < eps) return 0;
    if(a > b) return 1;
    return -1;
}

void solve(){
    cout << fixed << setprecision(10);
    if(n == 1){
        if(cmp(C[1], X) == 0){
            cout << V / R[1] << endl;
        }
        else {
            cout << "IMPOSSIBLE" << endl;
        }
        return;
    }
    else if(n == 2){
        long double t1 = V*(X-C[2]) / (R[1]*(C[1]-C[2]));
        long double t2 = V*(C[1]-X) / (R[2]*(C[1]-C[2]));
        if(C[1] == C[2]){
            if(C[1] == X) {
                cout << V / (R[1]+R[2]) << endl;
            }
            else {
                cout << "IMPOSSIBLE" << endl;
            }
            return;
        }
        //cout << t1 << " " << t2 << endl;
        if(cmp(t1, 0) == -1 || cmp(t2,0) == -1)
            cout << "IMPOSSIBLE" << endl;
        else{

            cout << max(t1, t2) << endl;
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif

    int sotest;
    cin >> sotest;
    FOR(test,1,sotest){
        cin >> n >> V >> X;
        FOR(i,1,n) cin >> R[i] >> C[i];
        cout << "Case #" << test << ": ";
        //if(test == 94) cout << n << endl;
        solve();
    }



    return 0;
}


