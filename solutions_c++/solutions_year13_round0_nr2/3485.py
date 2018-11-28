#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

bool bit(int64 mask, int k) {
    return ((1LL << k) & mask) != 0;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        cerr << "Case #" << testNumber << "..." << endl;
        int n, m;
        cin >> n >> m;
        vvi a(n, vi(m));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j)
                cin >> a[i][j];
        }

        bool res = true;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int h = a[i][j];
                bool hor = true, ver = true;
                for (int k = 0; k < m; ++k) {
                    if (a[i][k] > h) ver = false;
                }
                for (int k = 0; k < n; ++k) {
                    if (a[k][j] > h) hor = false;
                }
                if (!hor && !ver) {
                    res = false;
                    break;
                }
            }
        }

        cout << "Case #" << testNumber << ": " << (res ? "YES" : "NO") << endl;
    }

    return 0;
}