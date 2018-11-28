#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

vector<int> u[105];
char s[105];

int n, m;

double lgf[105];

double ch(int n, int k) {
    return lgf[n] - lgf[k] - lgf[n-k];
}

set<int> rt;
double dp[105];
int ss[105];

void f(int i) {
    ss[i] = 0;
    double res = 0;
    for (int j : u[i]) {
        f(j);
        res += dp[j];
        res += ch(ss[i]+ss[j], ss[j]);
        ss[i] += ss[j];
    }
    dp[i] = res;
    ss[i]++;
}

double cw() {
    double res = 0;
    int sus = 0;
    for (int j : rt) {
        res += dp[j];
        res += ch(sus+ss[j], ss[j]);
        sus += ss[j];
    }
    return res;
}

char cs[105];
int css;

void gen_rand() {
    rt.clear();
    for (int i : u[0]) rt.insert(i);
    double tw = dp[0];

    css = 0;
    while (sz(rt)) {
        double p = rand() / 1. / RAND_MAX;
        set<int> bup = rt;
        for (int i : bup) {
            rt.erase(i);
            for (int j : u[i]) rt.insert(j);
            double nw = cw();
            double prob = exp(nw - tw);
            p -= prob;
            //printf("i=%d\n", i);
            if (p <= 1e-9) {
                cs[css++] = s[i];
                tw = nw;
                break;
            }
            rt = bup;
        }
    }
}

string l[10];
int cnt[10];

int main() {
    lgf[0] = 0;
    FO(i,1,105) {
        lgf[i] = lgf[i-1] + log(i);
    }
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        scanf("%d", &n);
        FO(i,0,n+1) u[i].clear();
        FO(i,1,n+1) {
            int p; scanf("%d", &p);
            u[p].push_back(i);
        }
        scanf("%s", s+1);
        scanf("%d", &m);
        FO(i,0,m) {
            cin >> l[i];
            cnt[i] = 0;
        }

        f(0);

        int TR = 2000;
        FO(t,0,TR) {
            //fprintf(stderr, "t=%d\n", t);
            gen_rand();
            cs[css] = 0;
            FO(i,0,m) {
                FO(j,0,n-sz(l[i])+1) {
                    if (l[i] == string(cs+j,cs+j+sz(l[i]))) {
                        cnt[i]++;
                        break;
                    }
                }
            }
        }

        printf("Case #%d:", Z);
        FO(i,0,m) printf(" %.5lf", cnt[i] / 1. / TR);
        printf("\n");
        fflush(stdout);
    }
}

