#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for(int i = 0; i < (int)n; ++i)
#define repf(i, f, l) for(int i = f; i < (int)l; ++i)

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

#define DBG0(x)    {if(DEBUG){ cout << #x << ": " << x << "\t"; }}
#define DBG(x)     {if(DEBUG){DBG0(x); cout << endl;}}
#define DBG2(x, y) {if(DEBUG){DBG0(x); DBG(y);}}
#define DBG3(x, y, z) {if(DEBUG){DBG0(x); DBG2(y, z);}}
#define DBG4(w, x, y, z) {if(DEBUG){DBG0(w); DBG3(x, y, z);}}

template <class T>
ostream& operator<<(ostream& os, vector<T> xs){ for(T x: xs) os << x << ' '; return os; }
template <class S, class T>
ostream& operator<<(ostream& os, pair<S,T> st){ os << "(" << st.first << "," << st.second <<")"; return os; }

typedef vector<int> vint;
typedef vector<ll> vll;
typedef vector<ul> vul;
typedef vector<ull> vull;
typedef vector<bool> vbl;
typedef pair<int, int> pii;

bool valid(string s) {
    for (char c : s) if (c == '-') return false;
    return true;
}

string rev(string s) {
    rep (i, s.size()) {
        s[i] = (s[i] == '-') ? '+' : '-';
    }
    reverse(ALL(s));
    return s;
}

int sub_solve(int k, string s) {
    if (valid(s)) return k;
    for(int i = s.size(); --i >= 0; ){
        if (s[i] == '-') {
            s = s.substr(0, i + 1);
            break;
        }
    }
    if (s[0] == '-') {
        reverse(ALL(s));
        rep(i, s.size()) 
            s[i] = (s[i] == '-') ? '+' : '-';
        return sub_solve(k + 1, s);
    } else { 
        rep (i, s.size()) {
            if (s[i] == '-') {
                string sub = rev(s.substr(0, i));
                return sub_solve(k + 1, sub + s.substr(i));
            }
        }
    }
}

int solve() {
    string str;
    cin >> str;
    int n = str.size();
    return sub_solve(0, str);
}


int main(void){
    int n;
    cin >> n;
    rep (i, n) {
        printf("Case #%d: %d\n", i + 1, solve());
    }
    return 0;
}
