#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);

    long long a, n, j;
    cin >> a;
    int count;
    long long sum;
    long long temp;

    long long mod;

    long long k;

    vector<long long> ans;

    for (int i = 0; i < a; ++i) {

        cout << "Case #" + to_string(i + 1) + ":" << endl;
        count = 0;
        cin >> n >> j;

        for (k = 1 + (1 << (n - 1)); k < (1 << n); k += 2) {
            ans.clear();
            if (count == j) {
                break;
            }
            for (int d = 2; d <= 10; ++d) {
                sum = 0;
                temp = 1;
                for (int f = 0; f < n; ++f) {
                    sum += temp * (1 & (k >> f));
                    //cout << sum << endl;
                    temp *= d;
                }
                //cout << "---" << endl;
                mod = -1;
                for (int f = 2; f <= sqrt(sum); ++f) {
                    if (sum % f == 0) {
                        mod = f;
                        break;
                    }
                }
                if (mod == -1) {
                    break;
                }
                ans.push_back(mod);
            }
            if (ans.size() < 9) {
                continue;
            }
            ++count;
            for (int d = n - 1; d >= 0; d--)
                cout << ((k >> d) & 1);
            for (int d = 0; d < 9; ++d) {
                cout << " " << ans[d];
            }
            cout << endl;
        }


    }


    return 0;
}