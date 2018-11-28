#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for(int i = 0; i < (int)n; ++i)
#define repf(i, f, l) for(int i = f; i < (int)l; ++i)
#define repit(it, t) for(__typeof((t).begin()) it = (t).begin(); it != (t).end(); it++)

#define endl "\n"

#ifdef ONLINE_JUDGE
#define DEBUG false
#else
#define DEBUG true
#endif

#define pb emplace_back
#define lb lower_bound
#define ul unsigned long
#define ull unsigned long long
#define ll long long
#define INF 1000000007
#define MOD 1000000007
#define fs first
#define sd second

#define ALL(c) (c).begin(),(c).end()

#define DBG0(x) if(DEBUG){ cout << #x << ": " << x << "\t"; }
#define DBG(x) if(DEBUG){DBG0(x); cout << endl;}
#define DBG2(x, y) if(DEBUG){DBG0(x); DBG(y);}
#define DBG3(x, y, z) if(DEBUG){DBG0(x); DBG2(y, z);}
#define DBG4(w, x, y, z) if(DEBUG){DBG0(w); DBG3(x, y, z);}

template <class T>
ostream& operator<<(ostream& os, vector<T> xs){
    for(T x: xs) os << x << ' ';
    return os;
}

typedef vector<int> vint;
typedef vector<ll> vll;
typedef vector<ul> vul;
typedef vector<ull> vull;
typedef vector<bool> vbl;
typedef pair<int, int> pii;

int inver(vector<int> as, int pos){
    int ret = 0;
    repf(i, pos, as.size()){
        repf(j, i + 1, as.size()){
            if(as[i] < as[j]) ret++;
        }
    }
    return ret;
}

const int cl = 2000000001;
int solve(vector<int> as){
    int n = as.size();
    int mn = cl;
    rep(i, 1 << n){
        vector<int> bs;
        rep(j, n){
            if((1 << j) & i)
                bs.pb(cl - as[j]);
            else
                bs.pb(as[j]);
        }
        mn = min(inver(bs, 0), mn);
    }
    return mn;
}

int main(void){
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    rep(tt, t){
        int n;
        cin >> n;
        vector<int> as(n);
        rep(i, n) cin >> as[i];
        cout << "Case #" << tt + 1 << ": " << solve(as) << endl;
    }
    return 0;
}
