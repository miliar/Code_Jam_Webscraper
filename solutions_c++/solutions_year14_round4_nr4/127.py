#include <cstdio>
#include <cstring>
#include <algorithm>

int n, m;
int ans, num;
int a[10]; 
char s[10][11];

int size;
struct Node {
    int to;
    Node *next[26];
} pool[100000], *root[10];

Node *newNode() {
    memset(pool[size].next, 0, sizeof(pool[size].next));
    return &pool[size ++];
}

void add(Node *p, char *s) {
    for (int i = 0; 0 != s[i]; ++ i) {
        if (NULL == p -> next[s[i] - 'A']) 
            p -> next[s[i] - 'A'] = newNode();
        p = p -> next[s[i] - 'A'];
    }
}


void build() {
    bool flag[n];
    std :: fill(flag, flag + n, false);
    for (int i = 0; i < m; ++ i)
        flag[a[i]] = true;
    for (int i = 0; i < n; ++ i)
        if (!flag[i])
            return ;
    size = 0;
    for (int i = 0; i < n; ++ i)
        root[i] = newNode();
    for (int i = 0; i < m; ++ i) 
        add(root[a[i]], s[i]);
    int tot = size;
    if (ans == tot)
        ++ num;
    else if (ans < tot) {
        ans = tot;
        num = 1;
    }
}
void dfs(int now) {
    //printf("%d\n", now);
    if (now == m) {
        build();
    } else {
        for (int i = 0; i < n; ++ i) {
            a[now] = i;
            dfs(now + 1);
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d", &m, &n);
        for (int i = 0; i < m; ++ i)
            scanf("%s", s[i]);
        ans = -1;
        dfs(0);
        printf("Case #%d: %d %d\n", cas, ans, num);
    }
}
