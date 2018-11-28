#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <assert.h>
using namespace std;

void smain();
int main(){
#ifdef TASK
    //freopen(TASK".in","rt",stdin);
    freopen("/Users/ramis/Downloads/B-large.in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    const clock_t start = clock();
#endif
    smain();
#ifdef TASK
    cerr << "\nTotal Execution Time: " << float( clock () - start ) /  CLOCKS_PER_SEC << endl;
#endif
    return 0;
}

#ifndef M_PI
#define M_PI 3.14159265358979311599796346854418516
#endif
#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define int long long
#define LL long long
#define mp(a,b) make_pair(a,b)
#define INF 2305843009213693951LL
#define MOD 1000000007
#define EPS 1E-6
#define N 111
/* --------- END TEMPLATE CODE --------- */

char s[N];

int f1(string str) {
    int m = str.length();
    int i = m - 1;
    for (; i >= 0 && str[i] == '+'; --i);
    if (i < 0) return 0;
    if (i < m - 1) return f1(str.substr(0, i + 1));
    for (; i >= 0 && str[i] == '-'; --i);
    if (i < 0) return 1;
    for (i = 0; i < m && str[i] == '+'; ++i);
    int res = 0;
    if (i != 0) res += 1;
    forn(j, i) str[j] = '-';
    reverse(str.begin(), str.end());
    forn(j, m) str[j] = str[j] == '-' ? '+' : '-';
    return f1(str) + res + 1;
}

int solve1() {
    string str(s);
    return f1(str);
}

void smain() {
    int n;
    cin >> n;
    for (int cas = 1; cin >> s; ++cas) {
        int res = solve1();
        cout << "Case #" << cas << ": " << res << endl;
        cerr << "Case #" << cas << ": " << res << endl;
    }
}
