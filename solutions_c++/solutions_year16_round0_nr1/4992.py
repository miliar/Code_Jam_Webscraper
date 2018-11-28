#include <bits/stdc++.h>
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

using namespace std;

typedef pair<int,int>II;
typedef pair<int,II>PII;
template<class T> T gcd(T a, T b) {T r; while(b!=0) {r=a%b;a=b;b=r;} return a;}
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }

const double PI = 2*acos(0.0);
const double eps = 1e-9;
const int infi = 1e9;
const LL Linfi = (LL) 1e18;
const LL MOD = 1000000007;
#define maxn 100005


int n;
int xet[11];

void solve() {
    if(n == 0){
        cout << "INSOMNIA" << endl;
        return;
    }
    memset(xet, 0, sizeof(xet));
    int step = 0, cur = 0, ans;
    while(step < 10000){
        step++;
        cur += n;
        int tmp = cur;
        while(tmp > 0){
            xet[tmp%10] = 1;
            tmp /= 10;
        }
        int ok = 0;
        FOR(i,0,9) if(xet[i] == 0) ok = 1;
        if(ok == 0){
            cout << cur << endl;
            return;
        }
    }
    cout << "INSOMNIA" << endl;
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
        cin >> n;
        cout << "Case #" << test << ": ";
        solve();
    }



    return 0;
}


