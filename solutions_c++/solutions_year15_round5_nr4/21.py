#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int n;

bool check(long long a, vector<long long> &e, vector<long long> f) {
    if (a == 0) {
        for (int i = 0; i < (int)e.size(); ++i) {
            if (f[i] % 2 != 0) {
                return false;
            }
        }
        return true;
    }
    if (a < 0) {
        a = -a;
    }
    int nxt = 0;
    for (int i = 0; i < (int)e.size(); ++i) {
        if (f[i] == 0) {
            continue;
        }
        while (nxt < (int)e.size() && e[nxt] != e[i] + a) {
            ++nxt;
        }
        if (nxt >= (int)e.size() || e[nxt] != e[i] + a || f[nxt] < f[i]) {
            return false;
        }
        f[nxt] -= f[i];
    }
    return true;
}

void cut(long long a, vector<long long> &e, vector<long long> &f) {
    if (a == 0) {
        for (int i = 0; i < (int)e.size(); ++i) {
            f[i] /= 2;
        }
        return;
    }
    bool flag = false;
    if (a < 0) {
        a = -a;
        flag = true;
    }
    int nxt = 0;
    vector<long long> ne, nf;
    for (int i = 0; i < (int)e.size(); ++i) {
        if (f[i] == 0) {
            continue;
        }
        nf.push_back(f[i]);
        if (!flag) {
            ne.push_back(e[i]);
        } else {
            ne.push_back(e[i] + a);
        }
        while (nxt < (int)e.size() && e[nxt] != e[i] + a) {
            ++nxt;
        }
        f[nxt] -= f[i];
    }
    e = ne;
    f = nf;
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        vector<long long> e(n), f(n);
        for (int i = 0; i < n; ++i) {
            scanf("%I64d", &e[i]);
        }
        long long cnt = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%I64d", &f[i]);
            cnt += f[i];
        }
        static int id = 0;
        printf("Case #%d:", ++id);
        while (cnt >>= 1) {
            for (int i = 0; i < (int)e.size(); ++i) {
                if (check(e[i], e, f)) {
                    printf(" %I64d", e[i]);
                    cut(e[i], e, f);
                    break;
                }
            }       
        }
        printf("\n");
    }
    return 0;
}
