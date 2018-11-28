#include <bits/stdc++.h>
#include <cassert>

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

typedef struct {
    bool sig;
    char let;
} lt;

char succ(char a){
    if(a == 'k') return 'i';
    else return a + 1;
}

lt mul(lt a, lt b){
    lt ret;
    ret.sig = a.sig ^ b.sig;
    if(a.let == '1'){
        ret.let = b.let;
        return ret;
    }
    if(b.let == '1'){
        ret.let = a.let;
        return ret;
    }
    if(a.let == b.let) {
        ret.let = '1';
        ret.sig ^= true;
        return ret;
    }
    if(succ(a.let) == b.let){
        ret.let = succ(b.let);
        return ret;
    }
    if(a.let == succ(b.let)){
        ret.let = succ(a.let);
        ret.sig ^= true;
        return ret;
    }
    DBG("UNKO");
    assert(false);
}

int main(void){
    int T;
    cin >> T;
    repf(ccc, 1, T + 1){
        bool ans = false;
        int n, l;
        cin >> n >> l;
        string ss;
        {
            string str;
            cin >> str;
            rep(i, l) ss += str;
        }
        n *= l;

        vector<lt> vs(n);
        rep(i, n) vs[i] = { false, ss[i]};

        vector<lt> lst(n);
        lst[n - 1] = vs[n - 1];
        for(int i = n - 2; i >= 0; --i)
            lst[i] = mul(vs[i], lst[i + 1]);

        vector<lt> hd(n);
        hd[0] = vs[0];
        repf(i, 1, n)
            hd[i] = mul(hd[i - 1], vs[i]);

        rep(i, n){
            if(ans) break;
            if(hd[i].let == 'i'){
                lt cur = { false, '1' };
                repf(j, i + 1, n - 1){
                    cur = mul(cur, vs[j]);
                    if(ans) break;
                    if(cur.let == 'j'){
                        if(lst[j + 1].let == 'k'){
                            ans |= !(lst[j + 1].sig ^ cur.sig ^ hd[i].sig);
                        }
                    }
                }
            }
        }

        cout << "Case #" << ccc << ": " << (ans ? "YES" : "NO") << endl;
    }
    return 0;
}
