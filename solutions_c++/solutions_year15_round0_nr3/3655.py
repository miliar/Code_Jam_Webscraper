#include<bits/stdc++.h>
 
#define INF 1000000000
#define EPS 1e-9
#define sz(c) (int) (c).size()
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define uniq(c) sort(all(c)); (c).resize(unique(all(c)) - (c).begin())
#define lobo(c, x) (int) (lower_bound(all(c), (x)) - (c).begin())
#define upbo(c, x) (int) (upper_bound(all(c), (x)) - (c).begin())
 
#define pb push_back
#define mp make_pair
#define fi first
#define se second
 
using namespace std;

#ifdef DEBUG   
    #define wrap(a) a
    #define debug(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

    vector<string> split(const string& s, char c) {
        vector<string> v;
        stringstream ss(s);
        string x;
        while (getline(ss, x, c))
            v.emplace_back(x);
        return move(v);
    }

    void err(vector<string>::iterator it) { cout << endl; }
    template<typename T, typename... Args>
    void err(vector<string>::iterator it, T a, Args... args) {
        cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << ", ";
        err(++it, args...);
    }
#else
    #define debug(args...) 
    #define wrap(a) 
#endif
typedef long long ll;
typedef pair <int, int> ii;

#define q1 1
#define qi 2
#define qj 3
#define qk 4

int mul[5][5] = {
    {0, 0, 0, 0, 0},
    {0, q1, qi, qj, qk},
    {0, qi, -q1, qk, -qj},
    {0, qj, -qk, -q1, qi},
    {0, qk, qj, -qi, -q1}
};
int invsign[5] = {0, 1, -1, -1, -1};
const int MAXN = 10000;
char str[MAXN+2];
int nl;
int psum[MAXN+2];

string qToStr(int i) {
    string res = "";
    switch (abs(i)) {
        case 1: 
            res = "1";
            break;
        case qi:
            res = "i";
            break;
        case qj:
            res = "j";
            break;
        case qk:
            res = "k";
            break;
    }
    if ( i < 0 ) res = "-" + res;
    return res;
}

int multSg(int a, int b) {
    int res = mul[abs(a)][abs(b)];
    if ( a < 0 ) res *= -1;
    if ( b < 0 ) res *= -1;
    return res;
}

int mult(int l, int r) {
    int res = psum[r];
    if ( l > 0 ) {
        // sumr/sum(l-1) = psum[r] * psum[l-1]^-1
        int a = res, b = psum[l-1];
        res = multSg(invsign[b]*b, a);
    }
    return res;
}

int charToQ(char c) {
    switch(c) {
        case '1': 
            return q1;
        case 'i':
            return qi;
        case 'j':
            return qj;
        case 'k':
            return qk;
    }
}

bool solve() {
    // 0..bl-1, bl..br-1, br..nl-1
    for ( int bl = 1; bl < nl; ++bl )
        for ( int br = bl+1; br < nl; ++ br ) {
            int mull = mult(0, bl-1);
            int mulm = mult(bl, br-1);
            int mulr = mult(br, nl-1);
            wrap(printf("0..%2d=%s,\t%2d..%2d=%s,\t%2d..%2d=%s\n", 
                bl-1, qToStr(mull).c_str(), 
                bl, br-1, qToStr(mulm).c_str(), 
                br, nl-1, qToStr(mulr).c_str()););
            if ( mull == qi && mulm == qj && mulr == qk ) {
                return true;
            }
        } return false;
}

int main() {
    int ntc; scanf("%d", &ntc);
    for ( int tc = 0; tc < ntc; ++tc ) {
        int l, x; scanf("%d%d", &l, &x);
        scanf("%s", str);

        nl = l*x;
        for ( int i = l; i < nl; ++i ) {
            str[i] = str[i-l];
        }

        for ( int i = 0; i < nl; ++i ) {
            if ( i == 0 ) psum[i] = charToQ(str[i]);
            else psum[i] = multSg(psum[i-1], charToQ(str[i]));
            wrap(printf("psum[%d]=%s\n", i, qToStr(psum[i]).c_str()););
        }

        printf("Case #%d: %s\n", tc+1, solve() ? "YES" : "NO");
    }
    return 0;
}
