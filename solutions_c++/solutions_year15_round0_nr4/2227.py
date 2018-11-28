#define _CRT_SECURE_NO_WARNINGS
//#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
#define all(c) (c).begin(), (c).end()
#define loop(i,a,b) for(ll i=a; i<ll(b); i++)
#define rep(i,b) loop(i,0,b)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
template<class T> ostream & operator<<(ostream & os, vector<T> const &);
template<int n, class...T> typename enable_if<(n>=sizeof...(T))>::type _ot(ostream &, tuple<T...> const &){}
template<int n, class...T> typename enable_if<(n< sizeof...(T))>::type _ot(ostream & os, tuple<T...> const & t){ os << (n==0?"":" ") << get<n>(t); _ot<n+1>(os, t); }
template<class...T> ostream & operator<<(ostream & os, tuple<T...> const & t){ _ot<0>(os, t); return os; }
template<class T, class U> ostream & operator<<(ostream & os, pair<T,U> const & p){ return os << "(" << p.first << ", " << p.second << ") "; }
template<class T> ostream & operator<<(ostream & os, vector<T> const & v){ rep(i,v.size()) os << v[i] << (i+1==(int)v.size()?"":" "); return os; }
#ifdef DEBUG
#define dump(...) (cerr<<#__VA_ARGS__<<" = "<<mt(__VA_ARGS__)<<" ["<<__LINE__<<"]"<<endl)
#else
#define dump(...)
#endif
ll const mod = 1000000007;
ll const inf = 1LL<<60;

string const GA = "GABRIEL";
string const RI = "RICHARD";
string solve(int X, int R, int C){
    if(R>C) swap(R,C);
    if(X==1){
        if(R*C%X!=0) return RI;
        else return GA;
    }
    if(X==2){
        if(R*C%X!=0) return RI;
        else return GA;
    }
    if(X==3){
        if(R*C%X!=0) return RI;
        else {
            if((R==3 && C==3) || (R==3 && C==4) || (R==2 && C==3)) return GA;
            if((R==1 && C==3)) return RI;
        }
    }
    if(X==4){
        if(R*C%X!=0) return RI;
        else {
            if((R==4 && C==4) || (R==3 && C==4)) return GA;
            else return RI;
        }
    }
    dump(X,R,C);
    return "!!!";
}

int main(){
    int T;
    cin >> T;
    rep(i,T){
        int X,R,C;
        cin >> X >> R >> C;
        string ans = solve(X,R,C);
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
}
