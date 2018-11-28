#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

void solve(int test)
{
    printf("Case #%d: ", test);
    cerr << test << endl;

    double c, f, x;
    cin >> c >> f >> x;

    double t = 0;

    const int MAXN = 4000000;

    double ans = 1e+9;

    for (int i = 0; i <= MAXN; i++)
    {
        double cps = 2 + i * f;
        ans = min(ans, t + x / cps);
        t += c / cps;                    
    }

    cout << ans << endl;

}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    cout.precision(10);
    cout << fixed;

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}
