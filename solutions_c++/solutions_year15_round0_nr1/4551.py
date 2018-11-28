#define _CRT_SECURE_NO_WARNINGS
//#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
//#define int ll
//#define endl "\n"
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
template<class T> inline bool chmax(T & x, T const & y){ return x<y ? x=y,true : false; }
template<class T> inline bool chmin(T & x, T const & y){ return x>y ? x=y,true : false; }
#ifdef DEBUG
#define dump(...) (cerr<<#__VA_ARGS__<<" = "<<mt(__VA_ARGS__)<<" ["<<__LINE__<<"]"<<endl)
#else
#define dump(...)
#endif
// ll const mod = 1000000007;
// ll const inf = 1LL<<60;

int solve(int Smax, string S);
int solve_naive(int Smax, string S);
pair<int,string> generator();
bool test(int Smax, string S);

signed main(){
    srand(time(0));
    ios_base::sync_with_stdio(0); cin.tie(0);

    int T;
    cin >> T;
    vector<pair<int,string>> input(T);
    rep(i,T){
        int Smax;
        string s;
        cin >> Smax >> s;
        input[i] = mp(Smax,s);
    }

#ifdef TEST
    vector<int> refrun;
#endif

    {
        vector<int> output(T);
        rep(i,T){
            output[i] = solve(input[i].first, input[i].second);
        }
        rep(i,T){
            cout << "Case #" << i+1 << ": " << output[i] << endl;
        }
#ifdef TEST
        refrun = output;
#endif
    }

#ifdef TEST
    {
        vector<int> output(T);
        rep(i,T){
            output[i] = solve_naive(input[i].first, input[i].second);
            assert(output[i] == refrun[i]);
        }
    }
    {
        rep(i,10000000){
            int Smax;
            string S;
            tie(Smax, S) = generator();
            assert(test(Smax, S));
        }
    }
#endif
}

int solve(int Smax, string S_){
    vector<int> S(Smax+1);
    rep(i,Smax+1) S[i] = S_[i]-'0';
    int cur = S[0];
    int ans = 0;
    for(int i=1;i<=Smax;i++){
        int invite = max(0, i-cur);
        ans += invite;
        cur += S[i] + invite;
    }
    return ans;
}

int solve_naive(int Smax, string S_){
    vector<int> S(Smax+1);
    rep(i,Smax+1) S[i] = S_[i]-'0';
    int ans = 0;
    for(int i=1;i<=Smax;i++){
        int standing = 0;
        for(int j=0; j<i;j++){
            standing += S[j];
        }
        int invite = max(0, i-standing);
        S[0] += invite;
        ans += invite;
    }
    return ans;
}

pair<int,string> generator(){
    int Smax = 10;
    string S(Smax+1,'0');
    rep(i,Smax+1) S[i] = rand()%3 + '0';
    return mp(Smax,S);
}

bool test(int Smax, string S){
    int ref = solve(Smax, S);
    int out = solve_naive(Smax, S);
    return ref == out;
}
