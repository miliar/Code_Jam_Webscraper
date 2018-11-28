#include<bits/stdc++.h>
using namespace std;
char a[1024][1024];
int r, c;
char s[4] = {'^', '>', 'v', '<'};
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};
int finddir(int i0, int j0) {
    int res = -1;
    for(int k = 0; k < 4; k++) {
        int i = i0, j = j0;
        do{
            i += dr[k];
            j += dc[k];
        } while(i >= 0 && j >= 0 && i < r && j < c && a[i][j] == '.');
        if(i >= 0 && j >= 0 && i < r && j < c) {
            res = 1;
            if(s[k] == a[i0][j0])
                return 0;
        }
    }
    return res;
}
void solve() {
    scanf("%d%d", &r, &c);
    for(int i = 0; i < r; i++)
        scanf("%s", a[i]);
    int res = 0;
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++)
            if(a[i][j] != '.') {
                int f = finddir(i, j);
                if(f == -1) {
                    printf("IMPOSSIBLE\n");
                    return;
                }
                res += f;
            }
    printf("%d\n", res);
}
int main() {
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T;
    long long n;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solve();
    }
}
