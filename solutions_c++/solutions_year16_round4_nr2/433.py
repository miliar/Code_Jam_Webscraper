#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<double> p;

vector<double> sel;
double pp[300][300];

int main() {
    int T, tc;
    int n, k;
    double sol;

    cin >> T;
    for (tc = 1; tc <= T; tc++) {
        cout << "Case #" << tc << ": ";

        cin >> n >> k;

        p.clear();
        for (int i = 0; i < n; i++) {
            double tmp;
            cin >> tmp;
            p.push_back(tmp);
        }

        sort(p.begin(), p.end());
        sol = -1;
        for (int ll = 0; ll <= k; ll++) {
            sel.clear();

            for (int i = 0; i < ll; i++) {
                sel.push_back(p[i]);
            }
            for (int i = 0; i < k - ll; i++) {
                sel.push_back(p[n - i - 1]);
            }
            memset(pp, 0, sizeof(pp));
            pp[0][0] = 1;
            for (int i = 1; i <= k; i++) {
                for (int j = 0; j <= i; j++) {
                    pp[j][i - j] = 0;
                    if (i - j - 1 >= 0) {
                        pp[j][i - j] += pp[j][i - j - 1] * sel[i - 1];
                    } 
                    if (j - 1 >= 0) {
                        pp[j][i - j] += pp[j - 1][i - j] * (1 - sel[i - 1]);
                    }
                }
            }
            if (sol < pp[k / 2][k / 2])
                sol = pp[k / 2][k / 2];
        }
        cout << sol << endl;
    }
    return 0;
}
