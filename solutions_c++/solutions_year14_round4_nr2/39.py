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

#define NMAX 1005
int a[NMAX];

void solve(int test)
{
    printf("Case #%d: ", test);

    int n; cin >> n;
    forn(i, n) cin >> a[i];

    int l = 0, r = n - 1;

    int ans = 0;

    while (l < r)
    {
        int id = l;
        for (int i = l + 1; i <= r; i++)
            if (a[i] < a[id]) id = i;
        if (id - l < r - id)
        {
            ans += id - l;
            while (id > l)
            {
                swap(a[id], a[id - 1]); id--;
            }        
            l++;
        }
        else
        {
            ans += r - id;
            while (r > id)
            {
                swap(a[id], a[id + 1]); id++;
            }
            r--;
        }
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
