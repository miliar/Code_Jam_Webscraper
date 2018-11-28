#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

int T;

struct Red {
    string s;
    int c[100];
};

Red reduce(string s) {
    int x = 0;
    Red r;
    fill(r.c, r.c + 100, 0);
    r.c[0]++;
    r.s = string(1, s[0]);
    for (int i = 1; i < s.size(); i++)
        if (s[i] == s[i - 1])
            r.c[x]++;
        else {
            r.s += s[i];
            r.c[++x]++;
        }
    return r;
}

int main() {
    scanf("%d", &T);
    for (int t = 0; t++ < T;) {
        int N, tgt[100];
        string strs[100], S;
        Red red[100];
        bool win = true;

        scanf("%d", &N);
        for (int i = 0; i < N; i++)
            cin >> strs[i];

        red[0] = reduce(strs[0]);
        S = red[0].s;
        copy(red[0].c, red[0].c + S.size(), tgt);

        for (int i = 1; win && i < N; i++) {
            red[i] = reduce(strs[i]);
            if (S != red[i].s)
                win = false;
            else
                for (int j = 0; j < S.size(); j++)
                    tgt[j] += red[i].c[j];
        }
        printf("Case #%d: ", t);
        if (!win) {
            printf("Fegla Won\n");
            continue;
        }
        int work = 0;
        for (int j = 0; j < S.size(); j++) {
            tgt[j] = round(tgt[j] * 1.0 / N);
            //printf("Target for %d: %d\n", j, tgt[j]);
            for (int i = 0; i < N; i++)
                work += abs(tgt[j] - red[i].c[j]);
        }
        printf("%d\n", work);
    }
}
