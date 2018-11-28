// !!! Please compile using GCC.
// !!! May not compile under Visual Studio.
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int by_bitcount(int a, int b) {
    return __builtin_popcount(a) < __builtin_popcount(b);
}

vector<int> prev[1<<20];

int main() {

    int tc;
    cin >> tc;

    for (int t = 1; t <= tc; t++) {
        int k, n;
        cin >> k >> n;

        vector<int> haveKeys(k);
        for (int i = 0; i < k; i++) {
            cin >> haveKeys[i];
        }

        vector<int> lock(n);
        vector<vector<int> > contents(n);

        for (int i = 0; i < n; i++) {
            cin >> lock[i];
            int count;
            cin >> count;
            contents[i].resize(count);
            for (int j = 0; j < count; j++) {
                cin >> contents[i][j];
            }
        }

        for (int i = 0; i < (1<<20); i++) {
            prev[i].clear();
        }
        vector<int> bits(1<<n);
        for (int i = 0; i < bits.size(); i++) {
            bits[i] = i;
        }
        sort(bits.begin(), bits.end(), by_bitcount);

        for (int idx = 1; idx < bits.size(); idx++) {
            int bit_pattern = bits[idx];
            for (int last = (n-1); last >= 0; last--) {
                if ((bit_pattern & (1<<last)) == 0) {
                    continue;
                }
                int prev_bit_pattern = bit_pattern - (1<<last);
                if (prev[prev_bit_pattern].size() == 0 && prev_bit_pattern != 0) {
                    continue;
                }
                vector<int> keys = haveKeys;
                for (int i = 0; i < n; i++) {
                    if ((prev_bit_pattern & (1<<i)) != 0) {
                        for (int j = 0; j < contents[i].size(); j++) {
                            keys.push_back(contents[i][j]);
                        }
                    }
                }
                for (int i = 0; i < n; i++) {
                    if ((prev_bit_pattern & (1<<i)) != 0) {
                        keys.erase(find(keys.begin(), keys.end(), lock[i]));
                    }
                }
                bool ok = find(keys.begin(), keys.end(), lock[last]) != keys.end();
                if (ok) {
                    vector<int> candidate = prev[prev_bit_pattern];
                    candidate.push_back(last + 1);
                    if (prev[bit_pattern].size() == 0 || candidate < prev[bit_pattern]) {
                        prev[bit_pattern] = candidate;
                    }
                }
            }
        }

        if (prev[(1<<n)-1].size() == 0) {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        } else {
            vector<int> ans = prev[(1<<n)-1];
            cout << "Case #" << t << ":";
            for (int i = 0; i < ans.size(); i++) {
                cout << " " << ans[i];
            }
            cout << endl;
        }
    }

    return 0;
}

