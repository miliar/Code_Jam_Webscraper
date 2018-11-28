#include <cstdio>
#include <algorithm>
#include <string.h>

using namespace std;

struct Node {
   // void clear(){memset(next, 0, sizeof(next));};
    int next[26];
};

Node trie[10][100];
int tn[10];

char str[20][20];
int m, n;
int ans, cnt;

int a[10];

void insert(char str[], int id) {
    int root = 1;
    for (int i = 0; str[i] != 0; i++) {
        int ch = str[i] - 'A';
        if (trie[id][root].next[ch] == 0) {
            trie[id][root].next[ch] = ++tn[id];
            //trie[i][tn[id]].clear();
        }
        root = trie[id][root].next[ch];
    }
}

int Count() {
    memset(trie, 0, sizeof(trie));
    int tot = 0;
    for (int i = 0; i < n; i++) {
        tn[i] = 1;
       // trie[i][tn[i]].clear();
    }
    for (int i = 0; i < m; i++) {

        //printf("%d ", a[i]);
        insert(str[i], a[i]);
    }
    for (int i = 0; i < n; i++) {
        if (tn[i] > 1) tot += tn[i];
    }

       // printf(":%d\n", tot);
    return tot;
}

void Search(int x) {
    if (x == m) {
        int tot = Count();
        if (tot > ans) {
            ans = tot; cnt = 1;
        } else if (tot == ans) cnt++;
        return;
    }
    for (int i = 0; i < n; i++) {
        a[x] = i;
        Search(x + 1);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &m, &n);
        for (int i = 0; i < m; i++) scanf("%s", str[i]);
        ans = 0;
        cnt = 0;
        Search(0);
        printf("Case #%d: %d %d\n", cas, ans, cnt);
    }
    return 0;
}
