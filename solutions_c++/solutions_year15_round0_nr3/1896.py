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
const int c1 = 31;
#define maxn 100005

int n, m;
int a[maxn];
string s;

II mul(II a, II b){
    II c;
    c.fi = a.fi ^ b.fi;
    if(a.se == 2 && b.se == 2) c.fi ^= 1;
    else if(a.se == 2 && b.se == 4) c.fi ^= 1;
    else if(a.se == 3 && b.se == 2) c.fi ^= 1;
    else if(a.se == 3 && b.se == 3) c.fi ^= 1;
    else if(a.se == 4 && b.se == 3) c.fi ^= 1;
    else if(a.se == 4 && b.se == 4) c.fi ^= 1;

    int u = a.se, v = b.se;
    if(u > v) swap(u,v);
    if(u == v) c.se = 1;
    else if(u == 1) c.se = v;
    else if(u == 2) {
        if(v == 3) c.se = 4;
        else if(v == 4) c.se = 3;
    }
    else if(u == 3 && v == 4) c.se = 2;
    return c;
}

II mul2(II a, II b){
    II c;
    c.fi = a.fi ^ b.fi;
    if(a.se == 2 && b.se == 2) c.fi ^= 1;
    else if(a.se == 4 && b.se == 2) c.fi ^= 1;
    else if(a.se == 2 && b.se == 3) c.fi ^= 1;
    else if(a.se == 3 && b.se == 3) c.fi ^= 1;
    else if(a.se == 3 && b.se == 4) c.fi ^= 1;
    else if(a.se == 4 && b.se == 4) c.fi ^= 1;

    int u = a.se, v = b.se;
    if(u > v) swap(u,v);
    if(u == v) c.se = 1;
    else if(u == 1) c.se = v;
    else if(u == 2) {
        if(v == 3) c.se = 4;
        else if(v == 4) c.se = 3;
    }
    else if(u == 3 && v == 4) c.se = 2;
    return c;
}

void solve(){
    //II u = II(0,3), v = u;
    //II z = mul(u,v); cout << z.fi << " " << z.se << endl;

    string t = "";
    FOR(i,1,m) t += s;
    n = t.size(); t = '0'+t;
    FOR(i,1,n) {
        if(t[i] == 'i') a[i] = 2;
        else if(t[i] == 'j') a[i] = 3;
        else if(t[i] == 'k') a[i] = 4;
    }
    //FOR(i,1,n) cout << a[i] << " "; cout << endl;

    vector<int> A;
    set<int> S;
    II st = II(0,1), en = II(0,1);
    FOR(i,1,n){
        st = mul(st, II(0, a[i]));
        //cout << i << "  " << st.fi << " " << st.se << endl;
        if(st.fi == 0 && st.se == 2) A.pb(i);
    }
    FORD(i,n,1){
        en = mul2(en, II(0,a[i]));
        if(en.fi == 0 && en.se == 4) S.insert(i);
    }

    FO(i,0,A.size()){
        int x = A[i]+1;
        st = II(0,1);
        FOR(j,x,n){
            st = mul(st, II(0,a[j]));
            //cout << a[j] << "  " << st.fi << " " << st.se << endl;
            if(st.fi == 0 && st.se == 3 && S.find(j+1) != S.end()){
                //cout << A[i] << " " << j << endl;
                //cout << st.fi << " " << st.se << endl;
                cout << "YES" << endl;
                return;
            }
        }
    }

    cout << "NO" << endl;
    //FO(i,0,A.size()) cout << A[i] << " "; cout << endl;
    //FORV(i,S) cout << *i << " "; cout << endl;
}

int main(){
    ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int sotest = 0;
    cin >> sotest;
    FOR(test,1,sotest){
        cin >> n >> m;
        cin >> s;
        cout << "Case #" << test << ": ";
        solve();
    }

    return 0;
}

/**

*/
