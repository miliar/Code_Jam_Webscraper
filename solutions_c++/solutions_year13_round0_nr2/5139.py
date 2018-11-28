#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;
int t;
int n, m, a[110][110], b[110][110];
int row[110], col[110];

void r(int id, int h) {
    for(int i = 0; i < m; i++) if(b[id][i] > h) b[id][i] = h;
}
void c(int id, int h) {
    for(int i = 0; i < n; i++) if(b[i][id] > h) b[i][id] = h;
}
bool check() {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(a[i][j] != b[i][j]) return false;
        }
    }
    return true;
}
int main() {
    //freopen("B-large.in","r",stdin);
    //freopen("B-Large.out","w",stdout);
    scanf("%d", &t);
    for(int test = 1; test <= t; test++) {
        scanf("%d%d", &n, &m);
        memset(b,100,sizeof(b));
        memset(row,0,sizeof(row));
        memset(col,0,sizeof(col));
        int yes = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                scanf("%d", &a[i][j]);
                row[i] = max(row[i],a[i][j]);
            }
        }
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) col[i] = max(col[i],a[j][i]);
        }
        for(int i = 0; i < n; i++) {
            r(i,row[i]);
            if(check()) {
                yes = 1;
                break;
            }
        }
        if(yes) {
            printf("Case #%d: YES\n", test);
            continue;
        }
        for(int i = 0; i < m; i++) {
            c(i,col[i]);
            if(check()) {
                yes = 1;
                break;
            }
        }
        if(yes) printf("Case #%d: YES\n", test);
        else printf("Case #%d: NO\n", test);
    }
    //system("pause");
    return 0;
}
