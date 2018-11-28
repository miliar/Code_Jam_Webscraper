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
#include <stack>
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

// bool bit(int64 mask, int k) {
//     return ((1LL << k) & mask) != 0;
// }

std::vector< vector<int> > cmp;

bool mless(int i, int j) {
    return cmp[i][j] == -1 || cmp[i][j] == 0 && i < j;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCount;
    cin >> testCount;
    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int n;

        cin >> n;
        std::vector<int> A(n), B(n);
        for (int i = 0; i < n; ++i) cin >> A[i];
        for (int i = 0; i < n; ++i) cin >> B[i];


        cmp.assign(n, std::vector<int>(n));

        for (int i = 1; i < n; ++i) {
            int a = A[i];
            int last = -1;
            for (int j = 0; j < i; ++j) {
                if (A[j] >= a) {
                    cmp[j][i] = 1;
                    cmp[i][j] = -1;
                } else if (A[j] == a - 1) {
                    cerr << "a" << endl;
                    last = j;
                }
            }
            cerr << a << " " << last << endl;
            assert(last >= 0 || a == 1);
            if (last > 0) {
                cmp[i][last] = 1;
                cmp[last][i] = -1;
            }
        }

        for (int i = n - 2; i >= 0; --i) {
            int b = B[i];
            int last = -1;
            for (int j = n - 1; j > i; --j) {
                if (B[j] >= b) {
                    cmp[j][i] = 1;
                    cmp[i][j] = -1;
                } else if (B[j] == b - 1) {
                    last = j;
                }
            }
            assert(last >= 0 || b == 1);
            if (last > 0) {
                cmp[i][last] = 1;
                cmp[last][i] = -1;
            }
        }

        bool go = true;
        while (go) {
            go = false;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (cmp[i][j] != 0) continue;
                    for (int k = 0; k < n; ++k) {
                        if (cmp[i][k] * cmp[k][j] == 1) {
                            assert(cmp[i][k] == cmp[k][j]);
                            cmp[i][j] = cmp[i][k];
                            go = true;
                        }
                    }
                }
            }
        }
        cerr << "debug" << endl;
        std::vector<int> xinv(n);
        for (int i=  0; i < n; ++i) xinv[i] = i;
        cerr << "debug" << endl;

        sort(xinv.begin(), xinv.end(), mless);
        cerr << "debug" << endl;

        std::vector<int> x(n);
        for (int i = 0; i< n; ++i) {
            x[xinv[i]] = i + 1;
        }
        cerr << "debug" << endl;

        cout << "Case #" << testNumber << ":";
        for (int i = 0; i < n; ++i)
            cout << " " << x[i];
        cout << endl;
    }

    return 0;
}