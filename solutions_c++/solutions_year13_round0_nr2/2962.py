#include <iostream>
#include <cstdio>
#include <memory.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
using namespace std;
const int maxn = 102;
int map[maxn][maxn];
int m,n;

void read() {
    scanf("%d %d",&m,&n);
    for (int i=0;i<m;i++) {
        for (int j=0;j<n;j++) {
            scanf("%d",&map[i][j]);
        }
    }
    return;
}

bool check(int x,int y) {
    bool is = true;
    for (int i=0;i<m;i++) {
        if (map[i][y] > map[x][y]) {
            is = false;
            break;
        }
    }
    if (is) return true;

    is = true;
    for (int i=0;i<n;i++) {
        if (map[x][i] > map[x][y]) {
            is = false;
            break;
        }
    }
    return is;
}

void solve() {
    bool flag = true;
    for (int i=0;i<m;i++) {
        for (int j=0;j<n;j++) {
            if (check(i,j) == false) {
                flag = false;
                break;
            }
        }
        if (flag == false) break;
    }
    puts(flag ? "YES" : "NO");
    return;
}

int main() {
    //freopen("in.txt","r",stdin);
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int i=1;i<=cas;i++) {
        printf("Case #%d: ",i);
        read();
        solve();
    }
    return 0;
}
