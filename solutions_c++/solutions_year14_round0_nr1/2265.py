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
#define DBG0(x) if(DEBUG){ cout << #x << ": " << x << "\t"; }
#define DBG(x) if(DEBUG){DBG0(x); cout << endl;}
#define DBG2(x, y) if(DEBUG){DBG0(x); DBG(y);}
#define DBG3(x, y, z) if(DEBUG){DBG0(x); DBG2(y, z);}
#define DBG4(w, x, y, z) if(DEBUG){DBG0(w); DBG3(x, y, z);}

typedef vector<int> vint;
typedef vector<ll> vll;
typedef vector<ul> vul;
typedef vector<ull> vull;
typedef vector<bool> vbl;
typedef pair<int, int> pii;

inline string case_num(int t){
    ostringstream ret;
    ret << "Case #" << t << ": ";
    return ret.str();
}

string solve(vector<int> ans, vector<vector<vint>> cards){
    ostringstream oss;
    vint as(16, 0);
    rep(i, 2){
        for(int a: cards[i][ans[i] - 1])
            as[a - 1]++;
    }
    set<int> ret;
    rep(i, 16)
        if(as[i] == 2) ret.insert(i + 1);
    if(ret.size() == 1)
        oss << *(ret.begin()) << endl;
    if(ret.size() == 0)
        oss << "Volunteer cheated!" << endl;
    if(ret.size() > 1)
        oss << "Bad magician!" << endl;
    return oss.str();
}

int main(void){
    ios::sync_with_stdio(false);
    vector<string> ans;
    vector<future<string>> prcs;
    int t;
    cin >> t;
    rep(num, t){
        vint ans(2);
        vector<vector<vint>> cards(2, vector<vint>(4, vint(4)));
        rep(i, 2){
            cin >> ans[i];
            rep(j, 4) rep(k, 4) cin >> cards[i][j][k];
        }
#ifdef ONLINE_JUDGE
        prcs.pb(async(solve, ans, cards));
#else
        cout << case_num(num + 1) << solve(ans, cards);
#endif
    }
#ifdef ONLINE_JUDGE
    rep(i, t)
        cout << case_num(i + 1) << prcs[i].get();
#endif
    return 0;
}
