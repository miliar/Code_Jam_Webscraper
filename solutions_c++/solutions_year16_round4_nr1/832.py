
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const string impossible = "IMPOSSIBLE";
const char val[] = {'R', 'P', 'S'};

int N, R, P, S;
int cnt[16][3];

char winner(char x, char y) {
    if (x == 'R') return y == 'P' ? y : x;
    if (x == 'P') return y == 'S' ? y : x;
    if (x == 'S') return y == 'R' ? y : x;
    return 'Z';
}

string solve_naive() {
    string s = "";
    for (int i = 0; i < R; i++)
        s += 'R';
    for (int i = 0; i < P; i++)
        s += 'P';
    for (int i = 0; i < S; i++)
        s += 'S';
    sort(s.begin(), s.end());

    string best = impossible;
    do {
        string cur = s;
        bool passed = true;
        for (int j = 0; j < N; j++) {
            string nxt = "";
            for (int i = 0; i < cur.size(); i += 2) {
                //cout << cur[i] << " " << cur[i + 1] << endl;
                if (cur[i] == cur[i + 1]) {
                    passed = false;
                    break;
                }
                nxt += winner(cur[i], cur[i + 1]);
            }
            //cout << cur << " " << nxt << endl;
            if (!passed)
                break;
            cur = nxt;
        }
        //cout << cur << endl;
        if (passed) {
            best = s;
            break;
        }
    } while (next_permutation(s.begin(), s.end()));
    return best;
}

string solve() {
    cnt[0][0] = R;
    cnt[0][1] = P;
    cnt[0][2] = S;
    for (int i = 1; i <= N; i++) {
        int x = cnt[i - 1][0], y = cnt[i - 1][1], z = cnt[i - 1][2];
        cnt[i][0] = (x - y + z) / 2;
        cnt[i][1] = (x + y - z) / 2;
        cnt[i][2] = (-x + y + z) / 2;
        /*
        for (int j = 0; j < 3; j++)
            cerr << i << j << ": " << cnt[i][j] << endl;
        */
        if (cnt[i][0] < 0 || cnt[i][1] < 0 || cnt[i][2] < 0)
            return impossible;
    }

    string lineup = "";
    for (int j = 0; j < 3; j++) {
        if (cnt[N][j] == 1)
            lineup += val[j];
    }
    for (int i = N - 1; i >= 0; i--) {
        //cerr << lineup << endl;
        string next_lineup = "";
        for (int j = 0; j < lineup.size(); j++) {
            char c = lineup[j];
            if (c == 'P')
                next_lineup += "PR";
            else if (c == 'R')
                next_lineup += "RS";
            else if (c == 'S')
                next_lineup += "SP";
        }
        lineup = next_lineup;
    }
    //cerr << lineup << endl;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < (1 << N); j += 2 * (1 << i)) {
            string s1 = lineup.substr(j, 1 << i);
            string s2 = lineup.substr(j + (1 << i), 1 << i);
            if (s1 > s2) {
                for (int k = 0; k < (1 << i); k++) {
                    lineup[j + k] = s2[k];
                    lineup[j + k + (1 << i)] = s1[k];
                }
            }
        }
    }
    return lineup;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N >> R >> P >> S;
        cout << "Case #" << t << ": " << solve() << endl;
        //cout << "Case #" << t << ": " << solve_naive() << endl;
    }
}
