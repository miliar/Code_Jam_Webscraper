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
const LL MOD = 1<<12;
#define maxn 200005

int n, a, b, c;


string DFS(string type, int depth){
    if(depth == 0) return type;
    string x = DFS(type, depth-1);
    string y;
    if(type == "P") y = DFS("R", depth-1);
    else if(type == "R") y = DFS("S", depth-1);
    else if(type == "S") y = DFS("P", depth-1);
    string ans1 = x; ans1 += y;
    string ans2 = y; ans2 += x;
    return min(ans1, ans2);
}

void solve(){
    vector<string> ans;
    string ansP = DFS("P", n); //cout << ansP << endl;
    string ansR = DFS("R", n);
    string ansS = DFS("S", n);
    int demR = 0, demP = 0, demS = 0;
    FOR(i,0,ansP.size()-1){
        if(ansP[i] == 'R') demR++;
        else if(ansP[i] == 'P') demP++;
        else demS++;
    }
    if(demR == a && demP == b && demS == c) ans.pb(ansP);

    demR = 0, demP = 0, demS = 0;
    FOR(i,0,ansR.size()-1){
        if(ansR[i] == 'R') demR++;
        else if(ansR[i] == 'P') demP++;
        else demS++;
    }
    if(demR == a && demP == b && demS == c) ans.pb(ansR);

    demR = 0, demP = 0, demS = 0;
    FOR(i,0,ansS.size()-1){
        if(ansS[i] == 'R') demR++;
        else if(ansS[i] == 'P') demP++;
        else demS++;
    }
    if(demR == a && demP == b && demS == c) ans.pb(ansS);

    sort(ans.begin(), ans.end());
    if(ans.size() > 0)
        cout << ans[0] << endl;
    else  cout << "IMPOSSIBLE" << endl;
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
        cin >> n >> a >> b >> c;
        cout << "Case #" << test << ": ";
        solve();
    }


    return 0;
}
