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

int read()
{
    int mask = 0;
    int row; cin >> row;
    row--;
    forn(i, 4)
    {
        forn(j, 4)
        {
            int x; cin >> x;
            x--;
            if (i == row) mask |= (1 << x);
        }
    }
    return mask;
}

void solve(int test)
{
    printf("Case #%d: ", test);
    
    int mask1 = read();
    int mask2 = read();

    int mask = mask1 & mask2;

    vector<int> v;
    forn(i, 16)
    {
        if (mask & (1 << i)) v.pb(i);
    }

    if (v.empty())
        cout << "Volunteer cheated!\n";
    if (v.size() == 1)
        cout << v[0] + 1 << endl;
    if (v.size() > 1) 
        cout << "Bad magician!\n";
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
