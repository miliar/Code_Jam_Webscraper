/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_V = 2500;
bool ans[MAX_V + 1];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        for (int i = 1; i <= MAX_V; ++i) {
            ans[i] = false;
        }
        int n;
        cin >> n;
        for (int i = 0; i < 2 * n - 1; ++i) {
            for (int j = 0; j < n; ++j) {
                int v;
                cin >> v;
                ans[v] = not ans[v];
            }
        }
        cout << "Case #" << T << ":";
        for (int i = 1; i <= MAX_V; ++i) {
            if (ans[i]) {
                cout << ' ' << i;
            }
        }
        cout << endl;
    }
    return 0;
}
