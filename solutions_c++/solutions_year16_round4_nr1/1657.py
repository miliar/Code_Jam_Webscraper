#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < n; i++)
#define what_is(x) cerr << #x << ": " << x << endl;

#define file "f"

using namespace std;

int T, N, R, P, S;
string answer;
bool flag;

// alphabetic is P R S

void set_ans(string new_ans) {
    answer = new_ans;
    flag = true;
}

char get_winner(char ch1, char ch2) {
    if (ch1 == 'R') {
        if (ch2 == 'P')
            return ch2;
        return ch1;
    }
    if (ch1 == 'S') {
        if (ch2 == 'R')
            return ch2;
        return ch1;
    }
    if (ch1 == 'P') {
        if (ch2 == 'S')
            return ch2;
        return ch1;
    }
    return '1';
}

void check(string s) {
    if (flag)
        return;
    string winner = s;
    while (winner.length() != 1) {
        string winner1 = "";
        for (int i = 0; i < (int)winner.length(); i += 2) {
            if (winner[i] == winner[i + 1])
                return;
            winner1 += get_winner(winner[i], winner[i + 1]);
        }
        winner = winner1;
    }
    set_ans(s);
}

void gen(string s, int R, int P, int S) {
    if ((int)s.length() == N) {
        check(s);
        return;
    }
    if (flag)
        return;
    if (P > 0)
        gen(s + "P", R, P - 1, S);
    if (R > 0)
        gen(s + "R", R - 1, P, S);
    if (S > 0)
        gen(s + "S", R, P, S - 1);
}

int main(void) {
    freopen(file".in", "r", stdin);
    freopen(file".out", "w", stdout);

    ios_base::sync_with_stdio(false);

    cin >> T;
    forn(t, T) {
        cin >> N >> R >> P >> S;
        N = 1 << N;
        answer = "IMPOSSIBLE";
        flag = false;
        gen("", R, P, S);
        cout << "Case #" << t + 1 << ": " << answer << "\n";
    }

}
