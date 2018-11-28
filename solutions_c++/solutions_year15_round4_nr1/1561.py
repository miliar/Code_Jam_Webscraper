#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)

#define MOD 1000000007
#define INF 2000000000

const int MAXR = 110;
int rcnt[MAXR], ccnt[MAXR];

int T, R, C;

string row;

int main() {
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cin >> R >> C;

        vector<string> board;

        memset(rcnt, 0, sizeof rcnt);
        memset(ccnt, 0, sizeof ccnt);

        for (int i = 0; i < R; i++) { cin >> row; board.PB(row); }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                rcnt[i] += (board[i][j] != '.');
            }
        }

        for (int j = 0; j < C; j++) {
            for (int i = 0; i < R; i++) {
                ccnt[j] += (board[i][j] != '.');
            }
        }

        cout << "Case #" << t << ": ";

        bool ok = true;

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (board[i][j] != '.' && rcnt[i] == 1 && ccnt[j] == 1) {
                    ok = false;
                    break;
                }
            }
        }

        if (!ok) {
            cout << "IMPOSSIBLE\n";
        }
        if (ok) {
            int ires = 0;

            for (int i = 0; i < R; i++) {
                if (rcnt[i] == 0) continue;

                int f = -1, l = -1;
                
                for (int j = 0; j < C; j++) {
                    if (board[i][j] != '.') {
                        if (f == -1) f = j;
                        l = j;
                    }
                }

                if (board[i][f] == '<') board[i][f] = 'X';
                if (board[i][l] == '>') board[i][l] = 'X';
            }

            for (int j = 0; j < C; j++) {
                if (ccnt[j] == 0) continue;

                int f = -1, l = -1;

                for (int i = 0; i < R; i++) {
                    if (board[i][j] != '.') {
                        if (f == -1) f = i;
                        l = i;
                    }
                }

                if (board[f][j] == '^') board[f][j] = 'X';
                if (board[l][j] == 'v') board[l][j] = 'X';
            }

            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (board[i][j] == 'X') ires++;
                }
            }

            cout << ires << "\n";
        }
    }

    return 0;
}
