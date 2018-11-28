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

int ss[701];
int main(void){
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    vector<int> ans(t);
    for(int tt = 0; tt < t; ++tt){
        int n, x;
        cin >> n >> x;
        vector<int> s(n);
        rep(i, n) cin >> s[i];
        rep(i, 701) ss[i] = 0;
        rep(i, n) ss[s[i]]++;

        int ret = 0;
        repf(i, 1, x + 1){
            for(int j = x - i; j > 0 && ss[i] > 0; j--){
                while(ss[j] > 0 && ss[i] > 0){
                    if(i == j && ss[i] == 1) break;
                    ss[j]--;
                    ss[i]--;
                    ret++;
                }
            }
        }
        rep(i, x + 1){
            ret += ss[i];
        }
        cout << "Case #" << tt + 1 << ": " << ret << endl;
    }
    return 0;
}
