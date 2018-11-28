#include <bits/stdc++.h>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FOD(i,a,b) for(int i=a;i>b;i--)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define debug cout << "YES" << endl

using namespace std;

typedef pair<int,int>II;
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return __builtin_popcount(s);}
template<class T> T gcd(T a, T b){ T r; while (b != 0) { r = a % b; a = b; b = r; } return a;}

const long double PI = 2*acos(0.0);
const long double eps = 1e-15;
//const int infi = 1e9;
const LL Linfi = 1e18;
const LL MOD = 1000000007;
const int c1 = 31;
const int c2 = 37;
#define maxn 110010
typedef pair<LL,LL> PII;

string s;

void solve(int test){
    cout << "Case #" << test << ": ";
    cin >> s;
    int i = s.size() - 1;
    int ans = 1;
    while(i >= 0 && s[i] == '+') i--;
    if(i == -1) ans = 0;
    FORD(j, i, 1){
        if(s[j] != s[j-1]) ans++;
    }
    cout << ans << endl;
}

int main(){
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int test;
    cin >> test;
    FOR(i, 1, test) solve(i);

    return 0;
}
