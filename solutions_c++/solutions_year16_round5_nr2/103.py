#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

const int iter = 10000;

int n;
int pr[1024];
vector<int> to[1024];
char cc[1024];
int m;
vector<string> wds;
int ts[128];

int cnts[128];

int ats;
int ac;
bool av[128];

int ls;
int sofar;
char s[128];

int getts(int v) {
    if (ts[v] != -1) {
        return ts[v];
    }
    ts[v] = 1;
    for (int i = 0; i < (int) to[v].size(); ++i) {
        ts[v] += getts(to[v][i]);
    }
    return ts[v];
}

void go() {
    while (ls < n) {
        int w = rand() % ats;
        int b = 0;
        for (int i = 0; i < n; ++i) {
            if (av[i]) {
                if (w < ts[i]) {
                    // printf("Take %d for %d\n", i, ls);
                    s[ls++] = cc[i];
                    for (int j = 0; j < (int) to[i].size(); ++j) {
                        // printf("Trans %d -> %d\n", i, to[i][j]);
                        ++ac;
                        // printf("INC AC to %d\n", ac);
                        av[to[i][j]] = 1;
                        ats += ts[to[i][j]];
                    }
                    --ac;
                    ats -= ts[i];
                    // printf("DEC AC TO %d\n", ac);
                    av[i] = 0;
                    b = 1;
                    break;
                }
                w -= ts[i];
            }
        }
        if (!b) {
            printf("unbroken w %d ac %d on ls %d of %d\n", w, ac, ls, n);
        }
        // printf("Finish AC is %d\n", ac);
    }
    s[ls] = '\0';
    for (int i = 0; i < m; ++i) {
        cnts[i] += (strstr(s, wds[i].c_str()) != NULL);
    }
    return;
}

void solve() {
    int T;
    scanf("%d", &T);
    printf("%d\n", T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            to[i].clear();
        }
        ac = 0;
        memset(av, 0, sizeof(av));
        for (int i = 0; i < n; ++i) {
            scanf("%d", &pr[i]);
            --pr[i];
            if (pr[i] >= 0) {
                to[pr[i]].push_back(i);
            } else {
                ++ac;
                av[i] = 1;
            }
        }
        scanf("%s", cc);
        scanf("%d", &m);
        wds.resize(m);
        for (int i = 0; i < m; ++i) {
            char buf[128];
            scanf("%s", buf);
            wds[i] = buf;
        }
        memset(ts, -1, sizeof(ts));
        for (int i = 0; i < n; ++i) {
            if (ts[i] == -1) {
                getts(i);
            }
        }
        memset(cnts, 0, sizeof(cnts));
        for (int i = 0; i < iter; ++i) {
            ac = 0;
            ats = 0;
            memset(av, 0, sizeof(av));
            for (int i = 0; i < n; ++i) {
                if (pr[i] >= 0) {
                } else {
                    ++ac;
                    av[i] = 1;
                    ats += ts[i];
                }
            }
            ls = 0;
            sofar = 0;
            // printf("Start ac %d\n", ac);
            go();
        }
        printf("%d\n", m);
        for (int i = 0; i < m; ++i) {
            printf("%.10lf\n", (double) cnts[i] / iter);
        }
    }
}

int ms[128];
double dc[128][128];

int main(int argc, char *argv[]) {
    if (argv[1][0] == 'a') {
        int T;
        double tests = 0;
        memset(dc, 0, sizeof(dc));
        for (int i = 2; i < argc; ++i) {
            ++tests;
            FILE *f = fopen(argv[i], "r");
            fscanf(f, "%d", &T);
            for (int j = 0; j < T; ++j) {
                fscanf(f, "%d", &ms[j]);
                for (int k = 0; k < ms[j]; ++k) {
                    double x;
                    fscanf(f, "%lf", &x);
                    dc[j][k] += x;
                }
            }
            fclose(f);
        }
        for (int i = 0; i < T; ++i) {
            for (int j = 0; j < ms[i]; ++j) {
                dc[i][j] /= tests;
            }
        }
        for (int i = 0; i < T; ++i) {
            printf("Case #%d:", i + 1);
            for (int j = 0; j < ms[i]; ++j) {
                printf(" %.5lf", dc[i][j]);
            }
            printf("\n");
        }
    } else {
        int k;
        sscanf(argv[1], "%d", &k);
        srand(k);
        solve();
    }
    return 0;
}
