#include <iostream>

using namespace std;

int solve(string word, int n) {
    int len = word.size();
    int ans = 0;
    for (int i = 0; i < len; ++i) {
        for (int l = n; l <= len; ++l) {
            if (i + l > len) break;
            int cnt = 0;
            for (int j = 0; j < l; ++j) {
                char c = word[i + j];
                //cout << c;
                if (!(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')) {
                    ++cnt;
                    if (cnt == n) {
                        ++ans;
                        break;
                    }
                } else {
                    cnt = 0;
                }
            }
            //cout << " " << ans << endl;
        }
    }
    return ans;
}

int main() {
    int tn;
    cin >> tn;
    for (int tt = 1; tt <= tn; ++tt) {
        string word;
        int n;
        cin >> word >> n;
        cout << "Case #" << tt << ": " << solve(word, n) << endl;
    }
    return 0;
}
