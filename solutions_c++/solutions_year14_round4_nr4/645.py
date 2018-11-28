#include <cstdio>
#include <algorithm>
#include <cstring>

typedef long long LL;

const LL M = 1e9+7;

int Ts;

int ltn;
struct Trie {
    Trie *cld[26];
    int ts[26];
    void clear() {
        memset(cld, 0, sizeof(cld));
    }

    int add(char *str, int acc = 0);
} tnodes[1000000];


int Trie::add(char *str, int acc) {
    if (str[0] == '\0') return acc;

    int idx = str[0] - 'A';
    if (cld[idx] == NULL) {
        cld[idx] = &tnodes[ltn++];
        cld[idx]->clear();
        return cld[idx]->add(str+1, acc+1);
    } else
        return cld[idx]->add(str+1, acc);
}

void jizz() {
    int m, n;
    scanf("%d%d", &m, &n);

    char strs[10][12];

    for (int i = 0; i < m; ++i) {
        scanf("%s", strs[i]);
    }

    LL len = 0;
    LL count = 0;
    int at[10] = {0};

    for (; at[m] == 0; ) {
        int size = n;

        int cnt[10] = {0};
        int nd = 0;
        for (int i = 0; i < m; ++i)
            if (cnt[at[i]] == 0)
                nd += 1, cnt[at[i]] += 1;

        if (nd == n) {
            for (int i = 0; i < n; ++i)
                tnodes[i].clear();

            ltn = n;

            for (int i = 0; i < m; ++i)
                size += tnodes[at[i]].add(strs[i]);

            if (size > len)
                len = size, count = 1;
            else if (size == len)
                count += 1;
        }

        at[0] += 1;
        for (int i = 0; at[m] == 0 and at[i] == n; ++i) at[i] = 0, at[i+1] += 1;
    }


    printf("%d %d\n", (int)len, (int)count);

}

int main() {
    int T; scanf("%d", &T);

    for (int t = 0; t < T; ++t) {
        printf("Case #%d: ", t+1);
        jizz();
    }
    return 0;
}
