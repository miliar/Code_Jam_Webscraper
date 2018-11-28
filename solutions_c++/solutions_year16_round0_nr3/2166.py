#include <cstdio>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <complex>
#include <iomanip>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector<vector<int> > graph;
const int INF = 1000000000;
const ll MOD = 1000000009;
#define FILEIN "C.in"
#define FILEOUT "C.out"



int main() {
    freopen(FILEIN, "r", stdin);
    freopen(FILEOUT, "w", stdout);
    int tests;
    cin >> tests;
    for (int _ = 1; _ <= tests; ++_) {
        // Output answer
        int N, J;
        cin >> N >> J;
        cout << "Case #" << _ << ":\n";
        int inside_numbers = (N - 2) / 2;
        for (int mask = 0; mask < J; ++mask) {
            // cout << mask << endl;
            int masks[inside_numbers];
            for (int i = 0; i < inside_numbers; ++i) {
                masks[i] = (mask >> i) & 1;
            }
            cout << 1;
            for (int i = 0; i < inside_numbers; ++i) {
                cout << masks[i] << masks[i];
            }
            cout << 1;
            cout << " ";
            for (int i = 3; i <= 11; ++i) {
                if (i == 11) {
                    cout << i;
                } else {
                    cout << i << " ";
                }
            }
            cout << endl;
        }


    }
    return 0;
}
