#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <utility>

typedef long long ll;

using namespace std;

template<typename T>
T next() { T tmp; cin >> tmp; return tmp; }

int bc(int a) { return a == 0 ? 0 : a % 2 + bc(a / 2);}
int bit(int n, int k) { return (n >> k) & 1;}

void solve() {
    int n = next< int >();
    int k = next< int >();
    int k2 = k / 2;
    vector< double > p(n);
    generate(p.begin(), p.end(), next< double >);
    double ans = 0;
    for (int msk = 0; msk < (1 << n); ++msk) {
        if (bc(msk) == k) {
            double tmp = 0.0;
            for (int q = msk; q != 0; q = (q - 1) & msk) {
                if (bc(q) == k2) {
                    double cut = 1.0;
                    for (int j = 0; j < n; ++j) {
                        if (bit(msk, j) == 1) {
                            cut *= bit(q, j) ? p[j] : (1 - p[j]);
                        }
                    }
                    tmp += cut;
                }
            }
            ans = max(ans, tmp);
        }
    }
    cout.precision(20);
    cout << ans << endl;
    /*sort(p.begin(), p.end());
    vector< vector< double > > d(k2 + 1, vector< double >(k2 + 1, 0.0));
    vector< vector< double > > ds(k2 + 1, vector< double >(k2 + 1, 0.0));
    d[0][0] = 1.0;
    for (int i = 0; i < n; ++i) {
        for (int a = 0; a < d.size(); ++a) {
            copy(d[a].begin(), d[a].end(), ds[a].begin());
        }
        for (int a = 0; a < d.size(); ++a) {
            for (int b = 0; b < d[a].size(); ++b) {
                if (a == 0 && b == 0) {

                } else if (a == 0 && b != 0) {
                    ds[a][b] = max(ds[a][b], d[a][b - 1] * (1 - p[i]));    
                } else if (a != 0 && b == 0) {
                    ds[a][b] = max(ds[a][b], d[a - 1][b] * p[i]);    
                } else {
                    ds[a][b] = max(ds[a][b], d[a - 1][b] * p[i]);    
                    ds[a][b] = max(ds[a][b], d[a][b - 1] * (1 - p[i]));    
                }
            }
        }
        for (int a = 0; a < d.size(); ++a) {
            for (int b = 0; b < d[a].size(); ++b) {
                cout << ds[a][b] << " ";
            }
            cout << endl;
        }
        cout << endl;
        for (int a = 0; a < d.size(); ++a) {
            copy(ds[a].begin(), ds[a].end(), d[a].begin());
        }
    }
    cout.precision(20);
    cout << d[k2][k2] << endl;*/
}

int main() {
    int n = next< int >();
    for (int i = 1; i <= n; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
