#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>

using namespace std;

string S;
int T;

int cnt[300], res[10];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> S;
        memset(cnt, 0, sizeof cnt);

        for (int i = 0; i < S.size(); ++i)
            cnt[S[i]]++;

        res[0] = cnt['Z'];
        res[2] = cnt['W'];
        res[4] = cnt['U'];
        res[6] = cnt['X'];
        res[8] = cnt['G'];

        res[3] = cnt['R'] - res[0] - res[4];
        res[5] = cnt['F'] - res[4];
        res[7] = cnt['S'] - res[6];
        res[9] = cnt['I'] - res[5] - res[6] - res[8];
        res[1] = cnt['N'] - res[7] - 2 * res[9];

        cout << "Case #" << t << ": ";
        for (int i = 0; i < 10; ++i)
        for (int j = 0; j < res[i]; ++j)
            cout << i;
        cout << "\n";
    }
}
