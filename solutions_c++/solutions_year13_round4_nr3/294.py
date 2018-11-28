#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int n;
int a[2020];
int b[2020];
int g[2020][2020];

int d[2020];
int td;



int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        memset(g, 0, sizeof(g));
        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        for (int i = 0; i < n; ++i)
            cin >> b[i];
        
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (a[i] >= a[j])
                    g[j][i] = 1;
                if (b[i] <= b[j])
                    g[i][j] = 1;
            }
        }
        
        memset(d, 0, sizeof(d));
        for (int k = 1; k <= n; ++k) {
            vector<int> x;
            for (int i = 0; i < n; ++i) {
                if (a[i] <= k && b[i] <= k && d[i] == 0) {
                    int l = 1, r = 1;
                    for (int j = 0; j < n; ++j) {
                        if (d[j] != 0) {
                            if (j < i)
                                l = max(l, a[j] + 1);
                            if (j > i)
                                r = max(r, b[j] + 1);
                        }
                    }
                    if (l == a[i] && r == b[i])
                        x.push_back(i);
                }
            }

            for (int ii = 0; ii < x.size(); ++ii) {
                int i = x[ii];
                bool ok = true;
                for (int jj = 0; jj < x.size(); ++jj) {
                    int j = x[jj];
                    if (g[j][i] && j != i) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    d[i] = k;
                    break;
                }
            }
        }
        
        cout << "Case #" << t + 1 << ": ";
        for (int v = 0; v < n; ++v)
            cout << d[v] << " ";
        cout << "\n";
        
    }
    
    
    return 0;
}