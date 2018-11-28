#include <iostream>
#include <vector>
#include <string>
#include <climits>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int testcase = 0; testcase < T; testcase++) {
        int R, C, MAP[100][100];

        cin >> R >> C;
        for (int r = 0; r < R; r++) {
            string s;
            cin >> s;
            for (int c = 0; c < C; c++) {
                switch (s[c]) {
                case '^': MAP[r][c] = 1; break;
                case '>': MAP[r][c] = 2; break;
                case 'v': MAP[r][c] = 3; break;
                case '<': MAP[r][c] = 4; break;
                default:  MAP[r][c] = 0; break;
                }
            }
        }
        
#if 0
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                cout << MAP[r][c];
            }
            cout << endl;
        }
#endif

        bool impossible = false;
        int changes = 0;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                int a = MAP[r][c], b = 0;
                if (!a)
                    continue;
                for (int i = 0; i < R; i++) {
                    if (i == r || !MAP[i][c])
                        continue;
                    b |= i < r ? (1<<1) : (1<<3);

                }
                for (int j = 0; j < C; j++) {
                    if (j == c || !MAP[r][j])
                        continue;
                    b |= j < c ? (1<<4) : (1<<2);
                }
                if ((b & (1<<a)) == 0) {
                    if (b) {
                        changes++;
                    }
                    else {
                        impossible = true;
                        goto finish;
                    }
                }
            }
        }

finish:
        cout << "Case #" << testcase+1 << ": ";
        if (impossible)
            cout << "IMPOSSIBLE";
        else
            cout << changes;
        cout << endl;
    }
    return 0;
}

// vim: set sw=4:
