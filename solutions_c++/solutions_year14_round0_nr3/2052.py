#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair

#define ALL(x) (x).begin(),(x).end()
#define CLR(a,b) memset(a,b,sizeof(a))
#define REPN(x,a,b) for (int x=a; x<b;++x)
#define REP(x,b) REPN(x, 0, b)

#define dbg(x) cout << #x << " = " << x << endl;
#define dbg2(x, y) cout << #x << " = " << x << "  " << #y << " = " << y << endl;
#define dbg3(x, y, z) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << endl;
#define dbg4(x, y, z, w) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "  " << #w << " = " << w <<  endl;

#define MAX 105

typedef long long ll;

int my[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int mx[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };

int main() {
    int T;
    cin >> T;
    REPN(tc, 1, T+1) {
        int R, C, M, ny, nx;
        cin >> R >> C >> M;
        int sz = R*C;
        int A[sz], T[R][C], P[R][C], Z[R][C];
        REP(i, sz-M) A[i] = 0;
        REPN(i, sz-M, sz) A[i] = 1;
        int finish = 0;
        if (M == R*C - 1) {
            printf("Case #%d:\n", tc);
            REP(i, R) {
                REP(j, C) {
                    if (i == 0 && j == 0) printf("c"); 
                    else printf("*");
                }
                printf("\n");
            }
            continue;
        }
        do {
            REP(i, sz) T[i/C][i%C] = A[i];
            REP(i, R) {
                REP(j, C) if (T[i][j] == 0) {
                    P[i][j] = 0;
                    Z[i][j] = 0;
                    REP(k, 8) {
                        ny = my[k] + i;
                        nx = mx[k] + j;
                        if (ny >= 0 && ny < R && nx >= 0 && nx < C && T[ny][nx]) {
                            P[i][j]++;
                        }
                    }
                }
            }
            int error = 0, tZeros = 0;
            REP(i, R) {
                REP(j, C) if (T[i][j] == 0) {
                    int zeros = 0;
                    if (P[i][j]) {
                        REP(k, 8) {
                            ny = my[k] + i;
                            nx = mx[k] + j;
                            if (ny >= 0 && ny < R && nx >= 0 && nx < C && T[ny][nx] == 0 && P[ny][nx] == 0) {
                                zeros = 1;
                                break;
                            }
                        }
                        if (!zeros) { error = 1; break; }
                    }
                    else {
                        tZeros++;
                        if (tZeros > 1) {
                            REP(k, 8) {
                                ny = my[k] + i;
                                nx = mx[k] + j;
                                if (ny >= 0 && ny < R && nx >= 0 && nx < C && T[ny][nx] == 0 && P[ny][nx] == 0 && Z[ny][nx]) {
                                    zeros = 1;
                                    break;
                                }
                            }
                            if (!zeros) { error = 1; break; }
                        }
                        Z[i][j] = 1;
                    }
                }
                if (error) break;
            }
            if (!tZeros) error = 1;
            if (!error) {
                printf("Case #%d:\n", tc);
                if (tZeros) {
                    int puse = 0;
                    REP(i, R) {
                        REP(j, C) {
                            if (T[i][j] == 1) printf("*");
                            else if (P[i][j] == 0) {
                                if (!puse) printf("c"), puse = 1;
                                else printf(".");
                            }
                            else printf(".");
                        }
                        printf("\n");
                    }
                }
                finish = 1;
                break;
            }
        } while (next_permutation(A, A+sz));
        if (!finish) {
            printf("Case #%d:\n", tc);
            printf("Impossible\n");
        }
    }
}


