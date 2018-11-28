#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int n, r, p, s;
char ans[4100];
char tree[13][4100];

int check(char winner) {
    tree[0][0] = winner;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 1 << i; j++) {
            if (tree[i][j] == 'R') {
                tree[i+1][2*j] = 'R';
                tree[i+1][2*j+1] = 'S';
            }
            if (tree[i][j] == 'P') {
                tree[i+1][2*j] = 'P';
                tree[i+1][2*j+1] = 'R';
            }
            if (tree[i][j] == 'S') {
                tree[i+1][2*j] = 'S';
                tree[i+1][2*j+1] = 'P';
            }
        }
    }
    int cr = 0, cp = 0, cs = 0;
    for (int i = 0; i < 1 << n; i++) {
        if (tree[n][i] == 'R')
            cr++;
        if (tree[n][i] == 'P')
            cp++;
        if (tree[n][i] == 'S')
            cs++;
    }
    return cr == r && cp == p && cs == s;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d %d %d", &n, &r, &p, &s);
        char winner = 'I';
        if (check('R'))
            winner = 'R';
        else if (check('P'))
            winner = 'P';
        else if (check('S'))
            winner = 'S';
        if (winner == 'I') {
            printf("Case #%d: IMPOSSIBLE\n", t);
            continue;
        }
        vector<string> v[13];
        for (int i = 0; i < 1 << n; i++) {
            char aux[2];
            aux[0] = tree[n][i];
            aux[1] = 0;
            v[0].push_back(aux);
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < v[i-1].size(); j += 2) {
                if (v[i-1][j+1] < v[i-1][j])
                    swap(v[i-1][j], v[i-1][j+1]);
                v[i].push_back(v[i-1][j] + v[i-1][j+1]);
            }
        }
        printf("Case #%d: %s\n", t, v[n][0].c_str());
    }
}
