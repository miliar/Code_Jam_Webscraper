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

string solve(const double c, const double f, const double x){
    char ans[16];
    double cps = 2.0;
    double time = 0.0;

    if(x <= c){
        sprintf(ans, "%.7f\n", x / cps);
        return string(ans);
    }

    while(true){
        time += c / cps;
        if((x - c) / cps <= x / (cps + f)){
            sprintf(ans, "%.7f\n", time + (x - c) / cps);
            return string(ans);
        }
        cps += f;
    }
}

int main(void){
    ios::sync_with_stdio(false);
    vector<string> ans;
    vector<future<string>> prcs;
    int t;
    cin >> t;
    rep(num, t){
        double c, f, x;
        cin >> c >> f >> x;
#ifdef ONLINE_JUDGE
        prcs.pb(async(solve, c, f, x));
#else
        cout << case_num(num + 1) << solve(c, f, x);
#endif

    }
#ifdef ONLINE_JUDGE
    rep(i, t)
        cout << case_num(i + 1) << prcs[i].get();
#endif
    return 0;
}
