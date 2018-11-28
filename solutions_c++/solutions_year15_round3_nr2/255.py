#include <bits/stdc++.h>
using namespace std;

int T, s, k, l;

char key[110], target[110];

bool overlap(char *t, int sh) {
    for (int i = 0; t[sh + i]; ++i) {
        if (t[i] != t[sh + i]) return false;
    }
    return true;
}

int main() {
	cin >> T;
    cout << fixed << setprecision(8);
    for (int cs = 1; cs <= T; ++cs) {
        cin >> k >> l >> s;
        cin >> key >> target;

        int maxbnana = 0;

        int shift = l;
        for (int i = 1; i < l; ++i) {
            if (overlap(target, i)) {
                shift = i;
                break;
            }
        }

        maxbnana = (s - l) / shift + 1;

        double multiplier = 1;

        map<char, int> kcnt;
        for (int i = 0; key[i]; ++i) {
            ++kcnt[key[i]];
        }
        for (int i = 0; target[i]; ++i) {
            multiplier *= (double)kcnt[target[i]];
            if (kcnt[target[i]] == 0) {
                maxbnana = 0;
                break;
            }
        }

        double ans = multiplier * (double)(s - l + 1);
        while (l--) {
            ans /= (double)k;
        }
        ans = (double)maxbnana - ans;

        cout << "Case #" << cs << ": " << ans << endl;
    }
    return 0;
}
