#include <malloc.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <deque>
#include <list>
#include <string>
#include <cstdlib>
#include <queue>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <assert.h>
#include <stack>
#include <bitset>

#ifndef LOCAL_MACHINE
#define trace(a) void()
#define tracearr(a, b) void()
#else
#define debug
#include "/home/victor/Dropbox/Public/trace.cpp"
#endif

using namespace std;

#define forn(i,j) for(int i = 0; i < int(j); ++i)
#define ford(i,j) for(int i = int(j) - 1; i >= 0; --i)
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin(); i != (c).end(); ++i)
#define all(a) (a).begin(), (a).end()
#define sqr(a) ((a)*(a))
#define mp make_pair
#define pb push_back
#define fs first
#define sc second
#define y1 botva

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

int a[100][100];

int solve (int t) {
    int n, m;
    if (!(cin >> n >> m))
        return 0;
    printf("Case #%d: ", t);
    forn(i, n)
        forn(j, m)
            cin >> a[i][j];
    while (n > 0 && m > 0) {
        int mn = 101;
        forn(i, n)
            forn(j, m)
                mn = min(mn, a[i][j]);
        forn(i, n) {
            bool br = 0;
            forn(j, m) {
                if (a[i][j] == mn) {
                    bool vert = 1, horiz = 1;
                    forn (i1, n)
                        vert &= (a[i1][j] == a[i][j]);
                    forn(j1, m)
                        horiz &= (a[i][j1] == a[i][j]);
                    if (horiz) {
                        --n;
                        memmove(a[i], a[i + 1], 100 * (n - i) * sizeof(int));
                    } else if (vert) {
                        --m;
                        forn(i1, n)
                            memmove(a[i1] + j, a[i1] + j + 1, (m - j) * sizeof (int));
                    } else {
                        puts("NO");
                        return 1;
                    }
                    br = 1;
                    break;
                }
            }
            if (br)
                break;
        }
    }
    puts("YES");
	return 1;
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    forn(i, t)
	    solve(i + 1);
	return 0;
}

