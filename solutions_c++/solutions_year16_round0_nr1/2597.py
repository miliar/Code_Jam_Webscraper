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
#define FILEIN "A.in"
#define FILEOUT "A.out"



int main() {
    freopen(FILEIN, "r", stdin);
    freopen(FILEOUT, "w", stdout);
    int tests;
    cin >> tests;
    for (int _ = 1; _ <= tests; ++_) {
        // Output answer
        ll N;
        cin >> N;


        cout << "Case #" << _ << ": ";

        if (N == 0) {
            cout << "INSOMNIA";
        } else {
            bool f[10];
            for (int i = 0; i < 10; ++i) {
                f[i] = false;
            }

            int count = 0;
            while (true) {
                count++;
                ll value = N * count;
                string str = to_string(value);
                for (int i = 0; i < str.length(); ++i) {
                    f[str[i] - '0'] = true;
                }
                bool fl = true;
                for (int i = 0; i < 10; ++i) {
                    if (!f[i]) {
                        fl = false;
                    }
                }
                if (fl) {
                    break;
                }
            }
            cout << N * count;
        }
        cout << "\n";
    }
    return 0;
}
