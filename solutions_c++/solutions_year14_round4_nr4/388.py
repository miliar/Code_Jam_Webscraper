#include <iostream>
#include <algorithm>
using namespace std;
const int MAXN = 11111;
const int MAXM = 30, KIND = 26;
int n, m, num;
char s[MAXM];
char str[10][MAXM];

struct node {
    char* s;
    int prefix;
    bool isword;
    node* next[KIND];
    void init() {
        s = NULL;
        prefix = 0;
        isword = false;
        memset(next,0,sizeof(next));
    }
}a[MAXN*MAXM], *root[4];//根
void insert(node *root,char *s) {
    node *p = root;
    for (int i = 0;s[i];i++) {
        int x = s[i] - 'A';
        p->s = s+i;
        if (p->next[x] == NULL) {
            a[num].init();
            p->next[x] = &a[num++];
        }
        p = p->next[x];
        p->prefix++;
    }
    p->isword = true;
}
bool del(node *root,char *s) {
    node *p = root;
    for (int i = 0;s[i];i++) {
        int x = s[i] - 'A';
        if (p->next[x] == NULL)
            return false;
        p = p->next[x];
    }
    if (p->isword)
        p->isword = false;
    else
        return false;
    return true;
}
bool search(node *root,char* s) {
    node* p = root;
    for (int i = 0;s[i];i++) {
        int x = s[i] - 'A';
        if (p->next[x] == NULL)
            return false;
        p = p->next[x];
    }
    return p->isword;
}
int count(node *root,char *s) {
    node *p = root;
    for (int i = 0;s[i];i++) {
        int x = s[i] - 'A';
        if (p->next[x] == NULL)
            return 0;
        p = p->next[x];
    }
    return p->prefix;
}

int id[MAXM];
int has[5];
int maxNum = -1, maxWay = 0;

void dfs(int now, int m, int n) {
    if (now == m) {
        //for (int i = 0; i < m; i++) cout << id[i] << ' ';
        //cout << endl;
        for (int i = 0; i < n; i++) {
            if (has[i] == 0) {
                return;
            }
        }
        int numNode = 0;
        num = 0;
        for (int i = 0; i < n; i++) {
            root[i] = &a[num++];
            root[i]->init();
        }
        for (int i = 0; i < m; i++) {
            insert(root[id[i]], str[i]);
        }
        //printf("%d\n", num);
        numNode = num;
        if (numNode > maxNum) {
            maxNum = numNode;
            maxWay = 1;
        } else if (numNode == maxNum) {
            maxWay++;
        }
        return;
    }
    for (int i = 0; i < n; i++) {
        id[now] = i;
        has[i]++;
        dfs(now + 1, m, n);
        has[i]--;
    }
}

int main() {
    int cases;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        maxNum = -1, maxWay = 0;
        scanf("%d %d", &m, &n);
        getchar();
        for (int i = 0; i < m; i++) {
            gets(str[i]);
        }
        memset(has, 0, sizeof(has));
        dfs(0, m, n);
        printf("Case #%d: %d %d\n", T, maxNum, maxWay);
    }

}