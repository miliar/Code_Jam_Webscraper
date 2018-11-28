#include <iostream>
#include <fstream>
#include <vector>
#define NMAX 12
using namespace std;

int a[NMAX][NMAX];
vector<int> l[NMAX * 2];
bool viz[NMAX * 2], m[NMAX * 2], solved;
int N, M[NMAX][NMAX], Sol[NMAX];

void bkt(int k) {
    if(k == 2 * N) {
        for(int i = 1; i <= 2 *N; ++i)
            if(m[i] == 0) {
                if(i > N)
                    for(int j = 1; j <= N; ++j) {
                        Sol[j] = M[j][i - N];
                    }
                else
                    for(int j = 1; j <= N; ++j) {
                        Sol[j] = M[i][j];
                    }
                solved = 1;
            }
    }
    else {
        if(solved)
            return;
        for(int i = 1; i <= 2 * N; ++i) {
            if(m[i] == 1)
                continue;
            bool ok = 1;
            if(i <= N) {
                for(int j = 1; j <= N; ++j) {
                        if(k > 1)
                            if(M[i - 1][j] >= l[k][j] && m[i-1]) {
                                ok = 0; break;
                            }
                        if(k < N)
                            if(M[i + 1][j] <= l[k][j] && m[i+1]) {
                                ok = 0; break;
                            }
                        if(m[N + j] && M[i][j] != l[k][j]) {
                            ok = 0; break;
                        }
                }
                if(ok)
                    for(int j = 1; j <= N; ++j)
                        M[i][j] = l[k][j];
            }
            else {
                for(int j = 1; j <= N; ++j) {
                    if(m[j] && M[j][i - N] != l[k][j]) {
                        ok = 0; break;
                    }
                }
                if(ok)
                    for(int j = 1; j <= N; ++j) {
                        M[j][i - N] = l[k][j];
                    }
            }
            if(ok) {
                m[i] = 1;
                //viz[i] = 1;
                bkt(k+1);
                //viz[i] = 0;
                m[i] = 0;
            }
        }
    }
}

int main()
{
    //freopen("data.in", "rt",stdin);
    //freopen("data.out", "wt", stdout);
    int T, x;
    scanf("%d", &T);
    for(int j = 1; j <= T; ++j) {
        scanf("%d", &N);
        solved = 0;
        for(int i = 1; i <= 2*N; ++i) {
            l[i].clear();
            l[i].assign(N+2, 0);
            m[i] = 0;
            viz[i] = 0;
        }
        for(int i = 1; i < 2*N; ++i) {
            for(int k = 1; k <= N; ++k) {
                scanf("%d", &x);
                l[i][k] = x;
            }
        }
        bkt(1);
        cout<<"Case #"<<j<<": ";
        for(int i = 1; i <= N; ++i) {
            cout<<Sol[i]<<' ';
        }
        cout<<'\n';
    }
    return 0;
}
