#include <stdio.h>
#include <algorithm>
using namespace std;

#define REP(i, n) for(int i=0; i<(n); i++)
#define REPD(i, n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i, a, b) for( int i = a; i <= (b); i++)
#define FORD(i, a, b) for(int i=(a); i >= (b); i--)
#define VAR(a, b) __typeof(b) a=(b)
#define FORCOL(i, col) for(VAR(i, (col).begin()); i!=(col).end(); i++)
#define ZERO(x) memset(x, 0, sizeof x);
#define ALL(x) (x).begin(), (x).end()

#define PB push_back
#define ST first
#define ND second

typedef long long int LL;
typedef long double LD;


// globals
int n, m;
int ** state;


bool isEnd() {
    REP(i, n) {
        REP(j, m) {
            if (state[i][j] != state[0][0]) {
                return false;
            }
        }
    }
    return true;
}

bool covers(int r, int c, int dr, int dc, int number) {
    // printf("covers: %d %d %d %d %d   ::", r, c, dr, dc, number);
    while (r < n && c < m) {
        if (state[r][c] != number) {
            // printf("  false\n");
            return false;
        }
        r += dr;
        c += dc;
    }
    // printf("  true\n");
    return true;
}

bool isCorrect(int number) {
    // printf("isCorrect dla %d\n", number);
    bool covered[n][m];
    REP(i, n) {
        REP(j, m) {
            covered[i][j] = false;
        }
    }
    // dla kazdego wiersza
    REP(i, n) {
        // jezeli zaczyna sie na zadana liczbe
        // i leci do konca
        if (state[i][0] == number && covers(i, 0, 0, 1, number)) {
            REP(j, m) {
                covered[i][j] = true;
            }
        }
    }
    // dla kazdej kolumny
    REP(i, m) {
        // jezeli zaczyna sie na zadana liczbe
        // i leci do konca
        if (state[0][i] == number && covers(0, i, 1, 0, number)) {
            REP(j, n) {
                covered[j][i] = true;
            }
        }
    }
    REP(i, n) {
        REP(j, m) {
            if (state[i][j] == number) {
                if (covered[i][j] == false) {
                    return false;
                }
            }
        }
    }
    return true;
}


int main() {
    int t;
    scanf("%d\n", &t);
    REP(tt, t) {
        // input
        scanf("%d %d", &n, &m);
        
        state = new int*[n];
        REP(i, n) {
            state[i] = new int[m];
            REP(j, m) {
                scanf("%d", &state[i][j]);
            }
        }
        
        // solve
        bool succ = true;
        while (not isEnd()) {
            // znajdz minimum
            int mini = state[0][0];
            REP(i, n) {
                REP(j, m) {
                    mini = min(mini, state[i][j]);
                }
            }
            // sprawdz, czy minima ukladaja sie w linie
            if (isCorrect(mini) == false) {
                succ = false;
                break;
            } else {
                // zamieniam minima na kolejna wysokosc
                REP(i, n) {
                    REP(j, m) {
                        if (state[i][j] == mini) {
                            state[i][j] = 101;
                        }
                    }
                }
                mini = state[0][0];
                REP(i, n) {
                    REP(j, m) {
                        mini = min(mini, state[i][j]);
                    }
                }
                REP(i, n) {
                    REP(j, m) {
                        if (state[i][j] == 101) {
                            state[i][j] = mini;
                        }
                    }
                }
            }
        }
        if (succ) {
            printf("Case #%d: YES\n", tt+1);
        } else {
            printf("Case #%d: NO\n", tt+1);
        }
      
    }
    return 0;
}
