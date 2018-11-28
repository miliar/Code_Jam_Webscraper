#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
#include <queue>
using namespace std;

int step[1025];

int from(string s) {
    int res = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '+') {
            res = res * 2;
        } else {
            res = res * 2 + 1;
        }
    }

    return res;
}

string to(int num, int len) {
    string res = "";
    for (int i = 0; i < len; i++) {
        if (num % 2 == 1) {
            res = res + "-";
        } else {
            res = res + "+";
        }
        num /= 2;
    }
    reverse(res.begin(), res.end());
    return res;
}

int flip(int x, int len, int first) {
    string board = to(x, len);
    string res = board;

    cerr << "flip board = " << board << endl;
    for (int i = first; i >= 0; i--) {
        res[first - i] = board[i];
        if (res[first - i] == '+') {
            res[first - i] = '-';
        } else {
            res[first - i] = '+';
        }
    }

    cerr << "flip res = " << res << endl;

    return from(res);
}

int main(int argc, char *argv[])
{
    int T = 0;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        string board;
        cin >> board;
        memset(step, 0x7f, sizeof(step));
        cout << "Case #" << cas << ": ";

        queue <int> Q;
        int len = board.size();
        int x = from(board);
        Q.push(x);
        step[x] = 0;

        while (!Q.empty()) {
            x = Q.front();
            Q.pop();

            if (x == 0) {
                break;
            }

            int s = step[x] + 1;
            for (int i = 0; i < len; i++) {
                cerr << "i = " << i << endl;
                cerr << "len = " << len << endl;
                int y = flip(x, len, i);
                cerr << "y = " << y << endl;
                cerr << "s = " << s << endl;
                if (step[y] > s) {
                    step[y] = s;
                    cerr << "step[y] = " << step[y] << endl;
                    Q.push(y);
                }
            }
        }

        cout << step[0] << endl;
    }
    return 0;
}
