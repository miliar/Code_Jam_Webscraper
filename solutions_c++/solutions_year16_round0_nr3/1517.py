#include <bits/stdc++.h>

#define gcd __gcd
#define bitcount __builtin_popcountll
#define getcx getchar_unlocked
#define rep(i,j,n) for(i=j;i<n;i++)
#define tr(it,c) for(auto it=(c).begin();it!=(c).end();it++)
#define pb push_back
#define mp make_pair
#define uset unordered_set
#define umap unordered_map
#define fi first
#define sc second
#define ft first
#define DEBUG 0
#define sum(a) accumulate(all(a),0)
#define unique(a) unique(all(a))

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pi;
typedef pair<ll, ll> pill;
typedef pair<int, pi> pii;

template <class T> T& get(T &n) {
    cin >> n;
    return n;
}

#ifdef TRACE
template<class T> ostream& printContainer(ostream &o, const T &c) {
    tr(it, c) {
        o << *it << ' ';
    }
    return o;
}

template<class T> ostream& operator<<(ostream &o, const vector<T> &c) {return printContainer(o, c);}
template<class T> ostream& operator<<(ostream &o, const deque<T> &c) {return printContainer(o, c);}
template<class T> ostream& operator<<(ostream &o, const list<T> &c) {return printContainer(o, c);}
template<class T> ostream& operator<<(ostream &o, const set<T> &c) {return printContainer(o, c);}
template<class T> ostream& operator<<(ostream &o, const uset<T> &c) {return printContainer(o, c);}
template<class T> ostream& operator<<(ostream &o, const multiset<T> &c) {return printContainer(o, c);}
template<class T, class V> ostream& operator<<(ostream &o, const map<T, V> &c) {return printContainer(o, c);}
template<class T, class V> ostream& operator<<(ostream &o, const umap<T, V> &c) {return printContainer(o, c);}
template<class T, class V> ostream& operator<<(ostream &o, const pair<T, V> &c) {return (o << "(" << c.ft << "," << c.sc << ")");}

#define trace(x)                 cerr << #x << ": " << x << endl;
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
#else
#define trace(x)
#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)
#endif

const ll hell = 1000000007;
const ll INF = (ll)hell * hell;
const int MAXN = 1000;

string to_bin(ll N) {
    string ret;
    while (N) {
        if (N & 1) ret.push_back('1');
        else ret.push_back('0');
        N >>= 1;
    }
    reverse(ret.begin(), ret.end());
    return ret;
}
bool isPrime(string &s, int base, vector<int> &v) {
    //Test with first 10^6 numbers;
    for (int i = 2; i <= MAXN; ++i) {
        int L = s.length();
        ll poreal = 1, real = 0;
        int res = 0, po = 1;
        for (int j = L - 1; j >= 0; --j) {
            if (s[j] == '1') {
                res = (res + po)%i;
                real += poreal;
            }
            po = (base * po) % i;
            poreal = (poreal * base);
        }
        if (res == 0) {
            v.push_back(i);
            return false;
        }
    }
    return true;
}
bool check_for(string s, int base, vector<int> &v) {
    return isPrime(s, base, v);
}
void solve(int N, int J) {
    ll A = 1LL << N, B = 1LL << (N - 1);
    int printed = 0;
    for (ll i = B + 1; i < A; i += 2) {
        bool ans = false;
        vector< int > v;
        for (int j = 2; j <= 10; ++j)
            ans |= check_for(to_bin(i), j, v);
        if (!ans) {
            cout << to_bin(i) << " ";
            assert((int)v.size() == 9);
            for (int x : v) cout << x << " ";
            cout << "\n";
            ++ printed;
        }
        if (printed == J) return;
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        int N, J;
        cin >> N >> J;
        cout << "Case #" << tc << ":\n";
        solve(N, J);
    }
}
