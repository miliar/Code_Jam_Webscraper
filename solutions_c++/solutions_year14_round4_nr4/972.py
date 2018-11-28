#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

#define N 26

int n, m, way[N], maxNode, maxWay;
char word[N][N];

struct Node {
    Node *son[N];
    Node() {
        for (int i = 0; i < N; i++)
            son[i] = NULL;
    }
};
Node *root[N];

void insert(Node *root, char *word) {
    while (*word) {
        int id = (*word) - 'A';
        if (root->son[id] == NULL)
            root->son[id] = new Node();
        root = root->son[id];
        word++;
    }
}

int nodesCount(Node *root) {
    if (root == NULL)
        return 0;
    int result = 1;
    for (int i = 0; i < N; i++)
        result += nodesCount(root->son[i]);
    return result;
}

void solve() {
    int result = 0;
    for (int i = 0; i < m; i++)
        root[i] = NULL;
    for (int i = 0 ; i < n; i++){
        if(root[way[i]] == NULL)
            root[way[i]] = new Node();
        insert(root[way[i]], &word[i][0]);
    }
    for (int i = 0; i < m; i++)
        result += nodesCount(root[i]);

    if (result > maxNode) {
        maxNode = result;
        maxWay = 1;
    } else if (result == maxNode)
        maxWay++;
}

void dfs(int deep) {
    if (deep == n) {
        solve();
        return;
    }
    for (int i = 0; i < m; i++) {
        way[deep] = i;
        dfs(deep + 1);
    }
}

void init() {
    maxNode = maxWay = 0;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++)
        scanf("%s", &word[i][0]);
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int cas, ans = 0;
    scanf("%d", &cas);
    for (int _cas = 1; _cas <= cas; _cas++) {
        init();
        dfs(0);
        printf("Case #%d: %d %d\n", _cas, maxNode, maxWay);
    }
    return 0;
}
