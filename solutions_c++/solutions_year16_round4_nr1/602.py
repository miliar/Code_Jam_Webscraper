#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int M = 3;
int n;
int CNT[M];
int cnt[M];
const char choose[] = "PRS";

//P -> R, R -> S, S -> P
// P R S
string dfs(int i, int win) {

    if (i == 0) {
        cnt[win]++;
        return string() + choose[win];
    } 
    string L = dfs(i - 1, win);
    string R = dfs(i - 1, (win + 1) % 3);
    if (L < R) return L + R;
    return R + L;
}

int main() {
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n;
        cin >> CNT[1] >> CNT[0] >> CNT[2];
        string ans_str;
        for (int win = 0; win < M; win++) {
            bool ok = true;
            memset(cnt, 0, sizeof(cnt));
            string ret = dfs(n, win);
            for (int i = 0; i < M; i++) {
                //cout << cnt[i] << " ";
                if (cnt[i] != CNT[i]) {
                    ok = false;
                }
            }
            //cout << endl;
            if (ok) {
                if (ans_str == "" || ret < ans_str) ans_str = ret;
            }
        }
        if (ans_str == "") ans_str = "IMPOSSIBLE";
        cout << "Case #" << Case++ << ": " << ans_str << endl;
    }
    return 0;
}
