#include <bits/stdc++.h>
using namespace std;

struct Node{
    int d[26];
    Node(){memset(d, 0, sizeof d);}
};

struct Trie{
    int nt;
    Node t[2222];
    void reset(){nt = 0; t[0] = Node();}
};

int m, n;
int res, nres;
char a[11][15];
int na[11];
int gr[11];
Trie tree[5];

void process(){
    //printf("PROCESS \n");
    for (int j = 0; j < n; j++) tree[j].reset();
    for (int i = 0; i < m; i++){
        int tt = gr[i], c = 0;
        //printf("%d", tt);
        for (int j = 0; j < na[i]; j++){
            if (tree[tt].t[c].d[a[i][j] - 'A'] != 0){
                c = tree[tt].t[c].d[a[i][j] - 'A'];
            }
            else{
                c = tree[tt].t[c].d[a[i][j] - 'A'] = ++tree[tt].nt;
                tree[tt].t[c] = Node();
            }
        }
    }
    int all = 0;
    for (int j = 0; j < n; j++){
        all += tree[j].nt + 1;
        if (tree[j].nt == 0) return; // one set is empty
    }
    //printf(" all = %d\n", all);
    if (all > res) res = all, nres = 0;
    if (all == res) nres++;
}

void finds(int i){
    if (i == m){
        process();
        return;
    }
    for (int j = 0; j < n; j++){
        gr[i] = j;
        finds(i + 1);
    }
}

void solve(){
    scanf("%d%d", &m, &n);
    for (int i = 0; i < m; i++) scanf("%s", a[i]), na[i] = strlen(a[i]);
    res = -1; nres = -1;
    finds(0);
    printf("%d %d\n", res, nres);
}

int main(){
    freopen("D.inp", "r", stdin);
    freopen("D.out", "w", stdout);
    int t; scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
