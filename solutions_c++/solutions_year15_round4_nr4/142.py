#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <vector>

using namespace std;

int shift[11];
int n, m, M, ans;
int a[11], Ans[111][11];
bool v[111];

void printline(int x) {
    for(int i = 0; i < m; ++i) {
        printf("%d" , x/shift[i]%3);
    }
    printf("\n");
}

bool check(int x, int y, int z) {
    for(int i = 0; i < m; ++i) {
        int tx = x == -1 ? x : x/shift[i]%3;
        int ty = y/shift[i]%3;
        int tz = z == -1 ? z : z/shift[i]%3;
        int tyl, tyr;
        tyl = y/shift[(i-1+m)%m]%3;
        tyr = y/shift[(i+1)%m]%3;
        int now = (tyl == ty) + (tyr == ty) + (tx == ty) + (tz == ty);
        //printf("%d ", now);
        if(now != ty + 1) {
            return false;
        }
    }
    return true;
}

void print(int x) {
    printf("ans: \n");
    for(int i = 0; i < n; ++i, printf("\n")) {
        for(int j = 0; j < m; ++j) {
            printf("%d", Ans[x][i]/shift[j]%3);
        }
    }
}

void dfs(int x) {
    if(x == n) {
        if(check(a[x-2], a[x-1], -1)) {
            memcpy(Ans[ans], a, sizeof(a));
            ans++;
            //print();
        }
        return;
    }
    for(int i = 0; i < shift[m]; ++i) {
        if(check(a[x-2], a[x-1], i)) {
            a[x] = i;
            dfs(x + 1);
        }
    }
}

bool check2(int x, int y, int t) {
    for(int i = 0; i < m; ++i) {
        if(x/shift[(i+t)%m]%3 != y/shift[i]%3) {
            return false;
        }
    }
    return true;
}

bool check1(int x, int y) {
    for(int j = 1; j <= m; ++j) {
        bool flag = true;
        for(int i = 0; i < n; ++i) {
            for(int k = 0; k < m; ++k) {
                if(Ans[x][i]/shift[(k+j)%m]%3 != Ans[y][i]/shift[k]%3) {
                    flag = false;
                    break;
                }
            }
        }
        if(flag) {
            return true;
        }
    }
    return false;
}


void work(int testcase) {
    scanf("%d%d", &n, &m);
    ans = 0;
    M = shift[m];
    for(int i = 0; i < M; ++i)
        for(int j = 0; j < M; ++j) {
            if(check(-1, i, j)) {
                //printline(i), printline(j);
                a[0] = i, a[1] = j;
                dfs(2);
            }
        }
    int ans1 = ans;
    memset(v, 0, sizeof(v));
    for(int i = 0; i < ans; ++i)
        for(int j = i + 1; j < ans; ++j) {
            if(check1(i, j)) {
                v[i] = true;
                //print(i);
                //print(j);
                ans1--;
                break;
            }
        }
    printf("Case #%d: %d\n", testcase, ans1);
}

int main() {
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    int TC;
    shift[0] = 1;
    for(int i = 1; i <= 10; ++i) {
        shift[i] = shift[i-1] * 3;
    }
    scanf("%d", &TC);
    for(int i = 1; i <= TC; ++i) {
        work(i);
    }
}