#define FNAME ""

#include <bits/stdc++.h>

#define hash padjf9srpi
#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
#define pb push_back
#define mp make_pair
#define forn(i, n) for (int i = 0; i < (n); i++)
#define fornr(i, n) for (int i = (n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (a); i < (b); i++)
#define gcd __gcd
#define all(a) (a).begin(), (a).end()
 
#ifdef _WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair <int, int> pii;
typedef vector <int> vi;

template <class T> T sqr(const T &a) {return a * a;}

string chars[3] = {"P", "R", "S"};
const int P = 0, R = 1, S = 2;
int T, n, r, p, s;

bool ok(const string &str) {
    int p1 = 0, r1 = 0, s1 = 0;
    for (char c: str) {
        if (c == 'P')
            p1++;
        if (c == 'R')
            r1++;
        if (c == 'S')
            s1++;
    }
    return (p == p1) && (r == r1) && (s == s1);
}

string f(int n, int start) {
    if (n == 0)
        return chars[start];
    string result = chars[start];
    string s, t;
    if (start == P) 
        s = f(n - 1, P), t = f(n - 1, R);
    if (start == R)
        s = f(n - 1, R), t = f(n - 1, S);
    if (start == S)
        s = f(n - 1, P), t = f(n - 1, S);
    if (s > t)
        return t + s;
    return s + t;
}

int main()
{
#ifdef LOCAL
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
#endif
    double timer = clock();
    scanf("%d", &T);
    forn(qqq, T) {
        scanf("%d%d%d%d", &n, &r, &p, &s);
        string ans = "";
        string x;
        x = f(n, P);
        if (ok(x) && (ans == "" || x < ans))
            ans = x;
        x = f(n, R);
        if (ok(x) && (ans == "" || x < ans))
            ans = x;
        x = f(n, S);
        if (ok(x) && (ans == "" || x < ans))
            ans = x;
        printf("Case #%d: ", qqq + 1);
        if (ans == "")
            puts("IMPOSSIBLE");
        else
            printf("%s\n", ans.c_str());                                       
    }       
    cerr << 1.0 * (clock() - timer) / CLOCKS_PER_SEC;
}

