#include <iostream>
#include <vector>

using namespace std;

#define sz(v) (static_cast<int>((v).size()))

typedef long long li;

const int N = 250;

int n;
li k;

li z[N];

int a[N][N];

int main() {
    int tests;
    cin >> tests;

    for (int test = 0; test < tests; ++test) {
        cin >> n >> k;
            
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                a[i][j] = 0;

        z[n - 1] = 1;
        for (int v = n - 2; v >= 0; --v) {
            a[v][v + 1] = 1;
            z[v] = z[v + 1];
            for (int u = v + 2; u < n; ++u) {
                if (z[v] + z[u] <= k) {
                    z[v] += z[u];
                    a[v][u] = 1;
                } 
            }
        }

        cout << "Case #" << test + 1 << ": ";
        if (z[0] == k) {
            cout << "POSSIBLE\n";
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j)
                    cout << a[i][j];
                cout << endl;
            }
        } else {
            cout << "IMPOSSIBLE\n";
        }

    }



    return 0;
}                           