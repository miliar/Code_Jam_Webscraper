#include <iostream>
#include <set>
#include <vector>

using namespace std;

vector<int> v[2][120];
int T, n, m;
int a[120][120], b[120][120];

int main() {
    cin >> T;
    for(int t = 0; t < T; ++t) {
        cin >> n >> m;
        for(int i = 0; i < 2; ++i) {
            for(int j = 0; j < 120; ++j) {
                v[i][j].clear();
            }
        }
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                cin >> a[i][j];
                b[i][j] = 100;
            }
        }
        for(int i = 0; i < n; ++i) {
            set<int> S;
            for(int j = 0; j < m; ++j) {
                S.insert(a[i][j]);
            }
            int val = *S.rbegin();
            v[0][val].push_back(i);
        }
        for(int i = 0; i < m; ++i) {
            set<int> S;
            for(int j = 0; j < n; ++j) {
                S.insert(a[j][i]);
            }
            if (S.size() == 1) {
                int val = *S.begin();
                v[1][val].push_back(i);
            }
        }
        for(int q = 99; q >= 1; --q) {
            for(int i = 0; i < v[0][q].size(); ++i) {
                for(int j = 0; j < m; ++j) {
                    b[v[0][q][i]][j] = q;
                }
            }
            for(int i = 0; i < v[1][q].size(); ++i) {
                for(int j = 0; j < n; ++j) {
                    b[j][v[1][q][i]] = q;
                }
            }
        }
        bool fail = false;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                if (a[i][j] != b[i][j]) {
                    fail = true;
                }
            }
        }
        cout << "Case #" << t + 1 << ": ";
        if (fail) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
        }
    }
    return 0;
}
