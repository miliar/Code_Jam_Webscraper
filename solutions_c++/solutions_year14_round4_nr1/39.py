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

const int XMAX = 705;

multiset<int> s;

void solve(int test)
{
    printf("Case #%d: ", test);
    cerr << "Case #" << test << endl;

    int n, x;
    cin >> n >> x;

    forn(i, n)
    {
        int y;
        cin >> y;
        s.insert(y);
    }

    int ans = 0;
    while (!s.empty())
    {
        int s1 = (*s.begin());
        s.erase(s.begin());
        ans++;
        if (s.empty()) break;
        int s2 = x - s1;

        multiset<int>::iterator it = s.lower_bound(s2);
        if (it == s.end() || (*it) > s2)
        {
            if (it == s.begin()) continue;
            it--;
        }
        
        cerr << s1 << " " << (*it) << endl;

        s.erase(it);
    }

    cout << ans << endl;
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}
