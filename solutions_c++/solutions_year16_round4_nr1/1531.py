#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    string ans;
    string a(1<<12, '#'), b(1<<12, '#');
    string &fst = a;
    string &snd = b;
    for (int testCase = 0; testCase < T; ++testCase) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        //cout << n << r << p << s << " ";
        ans = "IMPOSSIBLE";
        for (char c: {'R', 'P', 'S'}) {
            fst[0] = c;
            for (int depth = 0; depth < n; ++depth) {
                for (int i = 0; i < (1 << depth); ++i) {
                    if (fst[i] == 'R') {
                        if (depth < n - 1) {
                            snd[2 * i] = 'S';
                            snd[2 * i + 1] = 'R';
                        } else {
                            snd[2 * i] = 'R';
                            snd[2 * i + 1] = 'S';
                        }
                    } else if (fst[i] == 'P') {
                        snd[2 * i] = 'P';
                        snd[2 * i + 1] = 'R';
                    } else if (fst[i] == 'S') {
                        if (depth < n - 2) {
                            snd[2 * i] = 'S';
                            snd[2 * i + 1] = 'P';
                        } else {
                            snd[2 * i] = 'P';
                            snd[2 * i + 1] = 'S';
                        }
                    }
                }
                swap(fst, snd);
            }
            int c_r = 0, c_p = 0, c_s = 0;
            for (int i = 0; i < (1<<n); ++i) {
                char c = fst[i];
                if (c == 'R') {
                    c_r++;
                } else if (c == 'P') {
                    c_p++;
                } else if (c== 'S') {
                    c_s++;
                }
            }
            if (c_r == r && c_p == p && c_s == s) {
                string t_ans = fst.substr(0, 1 << n);
                if (ans == "IMPOSSIBLE" || t_ans < ans) {
                    ans = t_ans;
                }
            }
        }
        cout << "Case #" << testCase + 1 << ": " << ans << endl;
    }
    return 0;
}
