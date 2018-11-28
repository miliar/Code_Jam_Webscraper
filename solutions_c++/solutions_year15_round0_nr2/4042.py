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

// 切るcutに固定してみる
// 切ったあとは空の皿に置くほうがいい
// 最初に切りまくってあとは放置するのがいい

// cut回以下の切断で最小の長さをlenにできるか？
// cut <- [0..sum[P[i]]], len <- [0..1000]
// 1000*1000*1000 * 100

bool check(int cut, int len, vector<int> const & P){
    int rem = cut;
    rep(i,P.size()){
        int c = P[i]%len==0 ? P[i]/len-1 : P[i]/len;
        if(rem < c) return false;
        rem -= c;
    }
    return true;
}

int solve(int D, vector<int> P){
    int ans1 = 1<<29;
#ifdef TEST
    int ans2 = 1<<29;
#endif
    int S = accumulate(all(P),0);
    for(int cut = 0; cut <= S; cut++){
        int len_l = 0;
        int len_r = 1010;
        int len_m;
        while(len_l + 1 < len_r){
            len_m = (len_l + len_r) / 2;
            if(check(cut, len_m, P)){
                len_r = len_m;
            } else {
                len_l = len_m;
            }
        }
        ans1 = min(ans1, cut + len_r);

#ifdef TEST
        for(int len = 1; len <= 1010; len++){
            if(check(cut, len, P)){
                ans2 = min(ans2, cut+len);
            }
        }
#endif
    }
#ifdef TEST
    if(ans1 != ans2){
        dump(ans1, ans2);
        dump(P);
        abort();
    }
#endif
    return ans1;
}

signed main(){
    int T;
    cin >> T;
    rep(i,T){
        int D;
        cin >> D;
        vector<int> P(D);
        rep(j,D) cin >> P[j];
        int x = solve(D,P);
        cout << "Case #" << i+1 << ": " << x << endl;
    }
}
