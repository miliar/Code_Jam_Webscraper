#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 60;

int tag;
int n;
int m;
struct node {
    int a[maxn];
    bool operator < (node b) const {
        int flag = 1;
        for(int i = tag; i <= n; i++) {
            int t = a[i] - b.a[i];
            if(t == 0)
                continue;
            if(t < 0) {
                flag = 1;
                break;
            }
            if(t > 0) {
                flag = 0;
                break;
            }
        }
        if(flag) {
            return true;
        } else {
            return false;
        }
    }
};

node a[2 * maxn];

int mp[maxn][maxn];
int key, flag;

int cmp(int a, int b, int c, int d) {
    int t1 = mp[a][b], t2 = mp[c][d];
    if(t1 == 0 || t2 == 0) {
        return 1;
    }
    if(t1 < t2) {
        return 1;
    }
    return 0;
}

int check() {
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            if(cmp(i, j, i, j + 1) == 0) {
                return 0;
            }
            if(cmp(i, j, i + 1, j) == 0) {
                return 0;
            }
        }
    }
    return 1;
}

void outPut() {
    if(flag == 0) {
        for(int i = 1; i <= n; i++) {
            printf(" %d", mp[key][i]);
        }
    } else {
        for(int i = 1; i <= n; i++) {
            printf(" %d", mp[i][key]);
        }
    }
    printf("\n");
}

int tmpCheck(int now, int pos, int flag) {
    int res = 1;
    if(flag == 0) {
        for(int i = 1; i <= n; i++) {
            if(mp[pos][i] == 0) {
                continue;
            }
            if(mp[pos][i] != a[now].a[i]) {
                res = 0;
                break;
            }
        }
    } else {
        for(int i = 1; i <= n; i++) {
            if(mp[i][pos] == 0) {
                continue;
            }
            if(mp[i][pos] != a[now].a[i]) {
                res = 0;
                break;
            }
        }
    }
    return res;
}

int dfs(int pos, int now) {
    if(pos == n + 1) {
        if(check()) {
            /*printf("------%d  %d\n", key, flag);
            for(int i = 1; i <= n; i++) {
                for(int j = 1; j <= n; j++) {
                    printf("%d ", mp[i][j]);
                }
                printf("\n");
            }*/
            return 1;
        }
        return 0;
    }
    tag = pos;
    sort(a + now, a + 1 + m);
    if(a[now].a[pos] == a[now + 1].a[pos]) {
        for(int i = pos; i <= n; i++) {
            mp[pos][i] = a[now].a[i];
            mp[i][pos] = a[now + 1].a[i];
        }

        if(check() && tmpCheck(now, pos, 0) && tmpCheck(now + 1, pos, 1)) {
            //printf("-------\n");
            if(dfs(pos + 1, now + 2)) {
                //printf("adsfsdfs");
                for(int i = 1; i <= n; i++) {
                    mp[pos][i] = a[now].a[i];
                    mp[i][pos] = a[now + 1].a[i];
                }
                return 1;
            }
        }


        for(int i = pos; i <= n; i++) {
            mp[pos][i] = a[now + 1].a[i];
            mp[i][pos] = a[now].a[i];
        }
        /*printf("*******\n");
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                printf("%d ", mp[i][j]);
            }
            printf("\n");
        }
        for(int i = 1; i <= n; i++) {
            printf("%d ", a[now].a[i]);
        }
        for(int i = 1; i <= n; i++) {
            printf("%d ", a[now + 1].a[i]);
        }*/
        //printf("check %d  %d  %d  %d\n", tmpCheck(now, pos, 1), tmpCheck(now + 1, pos, 0), now + 1, pos);
        if(check() == 0 || tmpCheck(now, pos, 1) == 0 || tmpCheck(now + 1, pos, 0) == 0) {
            return 0;
        }


        if(dfs(pos + 1, now + 2)) {
            //printf("adsfsdfs\n");
            for(int i = 1; i <= n; i++) {
                mp[pos][i] = a[now + 1].a[i];
                mp[i][pos] = a[now].a[i];
            }
            //printf("pos   %d\n", pos);
            return 1;
        } else {
            return 0;
        }

    } else {
        key = pos;
        flag = 0;
        mp[pos][pos] = a[now].a[pos];
        for(int i = pos + 1; i <= n; i++) {
            //mp[pos][i] = mp[pos - 1][i] + 1;
            mp[i][pos] = a[now].a[i];
        }

        if(check() && tmpCheck(now, pos, 1)) {
            if(dfs(pos + 1, now + 1) == 1) {

                //printf("nnnnnnnnnnnn\n");
                /*printf("*******\n");
                for(int i = 1; i <= n; i++) {
                    for(int j = 1; j <= n; j++) {
                        printf("%d ", mp[i][j]);
                    }
                    printf("\n");
                }*/
                return 1;
            }
        }
        for(int i = pos + 1; i <= n; i++) {
            mp[i][pos] = 0;
        }
        flag = 1;
        mp[pos][pos] = a[now].a[pos];
        for(int i = pos + 1; i <= n; i++) {
            mp[pos][i] = a[now].a[i];
            //mp[i][pos] = mp[i][pos - 1] + 1;
        }
        if(check() && tmpCheck(now, pos, 0)) {
            if(dfs(pos + 1, now + 1)) {
                return 1;
            } else {
                for(int i = pos + 1; i <= n; i++) {
                    mp[pos][i] = 0;
                }
                return 0;
            }
        }
    }
}

void solve() {
    memset(mp, 0, sizeof(mp));
    m = 2 * n - 1;
    int tmp = dfs(1, 1);
    if(tmp == 0) {
        printf("_______________________________\n");
    }
    //printf("--- %d %d  %d\n", tmp, key, flag);
    outPut();
}

int main() {
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("Bout.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int _ = 1; _ <= t; _++) {
        printf("Case #%d:", _);
        scanf("%d", &n);
        for(int i = 1; i <= 2 * n - 1; i++) {
            for(int j = 1; j <= n; j++) {
                scanf("%d", &a[i].a[j]);
            }
        }
        solve();
    }
    return 0;
}


