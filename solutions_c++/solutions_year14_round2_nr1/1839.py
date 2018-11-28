#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstring>
#include <fstream>
#include <ctime>
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
#define MOD 1000000007
#define maxn 10000005

int n;
string s[105], t[105];

string chuan_hoa(string s){
    s = s + '_';
    string ans = "";
    FO(i,0,s.size()-1){
        if(s[i] != s[i+1]) ans += s[i];
    }
    return ans;
}

int sosanh(string s, string t){
    int i = 0, j = 0, ans = 0;
    while(1){
        if(s[i] == t[j]) {
            char tmp = s[i];
            int cnt1 = 0, cnt2 = 0;
            while(1){
                if(s[i] == tmp) {i++; cnt1++;}
                else if(i == s.size()) break;
                else break;
            }
            while(1){
                if(t[j] == tmp) {j++; cnt2++;}
                else if(j == t.size()) break;
                else break;
            }
            ans += abs(cnt1 - cnt2);
        }
        else break;
        //cout << i << " " << j << endl;
        if(i == s.size() && j == t.size()) break;
    }

    //cout << ans << endl;
    return ans;
}

void solve(){
    int ans = 0;
    set<string> S;
    FOR(i,1,n) {t[i] = chuan_hoa(s[i]); S.insert(t[i]);}
    if(S.size() >= 2) {cout << "Fegla Won" << endl; return;}

    string goc = *S.begin();
    FOR(i,1,n) ans += sosanh(goc, s[i]);

    FOR(i,1,n){
        int tmp = 0;
        FOR(j,1,n) if(i != j){
            tmp += sosanh(s[i], s[j]);
        }
        ans = min(ans, tmp);
    }
    cout << ans << endl;
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int sotest = 1;
    cin >> sotest;
    FOR(test,1,sotest){
        cin >> n; cin.ignore(1);
        FOR(i,1,n) cin >> s[i];
        cout << "Case #" << test << ": ";
        solve();
    }



    return 0;
}

