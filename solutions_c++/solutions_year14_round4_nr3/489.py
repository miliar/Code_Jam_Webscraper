#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define MAXX 110
#define MAXY 510
#define MAXN (MAXX*MAXY*10)

int a[MAXX][MAXY];
int num[MAXX][MAXY];
int n, fin, k;

vector< pii > f[MAXN];
vector< pii > c[MAXN];
vector<int>   back[MAXN];
int o[MAXN];
int nn[MAXN];
int from[MAXN];
int x, y, b;

int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};

int get_fc(int i, int j, int &F, int &C) {
    int ind = lower_bound(f[i].begin(), f[i].end(), make_pair(j, -1)) - f[i].begin();
    if (ind == f[i].size()) {
        F = C = 0;
        return -1;
    }
    if (f[i][ind].first == j) {
        F = f[i][ind].second;
        C = c[i][ind].second;
        return ind;
    }

    F = C = 0;
    return -1;
}

void add(int i, int j) {
    f[i].push_back( make_pair(j, 0) );
    c[i].push_back( make_pair(j, 1) );
    back[j].push_back(i);
}

int can(int i, int j) {
    int f1, c1, f2, c2;
    get_fc(i, j, f1, c1);
    get_fc(j, i, f2, c2);
    if (c1 - f1 + f2 > 0) return 1;
    return 0;
}

int find_flow() {
    int res = 0;
    while (true) {
        memset(nn, 0, sizeof(nn));
        int tail = 0;
        int head = 0;
        o[tail] = 0;
        nn[0] = 1;
        from[0] = 0;
        while (tail <= head && !nn[fin]) {
            int v = o[tail];
            //printf("%i %i\n", v/4, v % 4);
            for(int j=0; j<f[v].size(); ++j) {
                int y = f[v][j].first;
                if (nn[y]) continue;
                if (can(v, y)) {
                    ++head;
                    o[head] = y;
                    nn[y] = 1;
                    from[y] = v;
                }
            }           

            for(int j=0; j<back[v].size(); ++j) {
                int y = back[v][j];
                if (nn[y]) continue;
                if (can(v, y)) {
                    ++head;
                    o[head] = y;
                    nn[y] = 1;
                    from[y] = v;
                }
            }           

            tail++;
        }

        if (!nn[fin]) break;
        res++;
        int y = fin;
        while (y != 0) {
            int x = from[y];
            int f1, c1;
            int ind = get_fc(x, y, f1, c1);
            if (f1 < c1) {
                f[x][ind].second++;
            } else {
                ind = get_fc(y, x, f1, c1);
                if (!f1) {
                    printf("FUCK!\n");
                    return -1000;
                }
                f[y][ind].second--;
            }
            y = x;
        }
    }
    return res;
}

int main(){
    int tc;
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("C-small-attempt2.out", "w", stdout);

    //freopen("c.in", "r", stdin);
    //freopen("c.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        fprintf(stderr, "%i\n", tt);
        scanf("%i %i %i", &x, &y, &b);
        k = x*y*10 + 20;
        
        for(int i=0; i<k; ++i) {
            f[i].clear();
            c[i].clear();
            back[i].clear();
        }

        memset(a, 0, sizeof(a));

        for(int i=0; i<b; ++i) {
            int xx1, yy1, xx2, yy2;
            scanf("%i %i %i %i", &xx1, &yy1, &xx2, &yy2);
            for(int i1=xx1; i1<=xx2; ++i1)
                for(int j1=yy1; j1<=yy2; ++j1)
                    a[i1][j1] = 1;
        }

            int k = 0;
            for(int j=0; j<y; ++j)
                for(int i=0; i<x; ++i) {
                    num[i][j] = ++k;
                    add(k*10 + 0, k*10 + 4);
                    add(k*10 + 1, k*10 + 4);
                    add(k*10 + 2, k*10 + 4);
                    add(k*10 + 3, k*10 + 4);

                    add(k*10 + 4, k*10 + 5);

                    add(k*10 + 5, k*10 + 6);
                    add(k*10 + 5, k*10 + 7);
                    add(k*10 + 5, k*10 + 8);
                    add(k*10 + 5, k*10 + 9);

                }

            ++k;
            fin = k*10;

            for(int i=0; i<x; ++i) {
                if (a[i][0] == 0) add(0, num[i][0]*10 + 0);
                if (a[i][y-1] == 0) add(num[i][y-1]*10 + 9, fin);
            }

            for(int j=0; j<y; ++j) 
                for(int i=0; i<x; ++i) if (a[i][j] == 0) {
                    for(int q=0; q<4; ++q) {
                        int i1 = i + dx[q];
                        int j1 = j + dy[q];
                        if (i1 >= 0 && i1 < x && j1 >=0 && j1 < y) {
                            if (a[i1][j1] == 0) {
                                add(num[i][j]*10 + 6 + q, num[i1][j1]*10 + 3 - q);
                            }
                        }
                    }
                }

            for(int i=0; i<=fin; ++i) {
                sort(f[i].begin(), f[i].end());
                sort(c[i].begin(), c[i].end());
            }
        

        printf("Case #%i: ", tt);        
        printf("%i\n", find_flow());
    }

    return 0;
}

