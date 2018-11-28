#include <bits\stdc++.h>
using namespace std;
const int N = 105;
int T;
int n, m;
int a[N][N];
int cnt1[N];
int cnt2[N];
int ans;
int main()
{
    freopen("A-large.in", "r", stdin); freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for(int qw = 1; qw <= T; ++qw){
        ans = 0;
        memset(a, 0, sizeof(a));
        memset(cnt1, 0, sizeof(cnt1));
        memset(cnt2, 0, sizeof(cnt2));
        cin >> n >> m;
        string s;
        for(int i = 1; i <= n; ++i){
            cin >> s;
            for(int j = 1; j <= m; ++j){
                if(s[j - 1] == '.'){
                    a[i][j] = 5;
                }
                else if(s[j - 1] == '^'){
                    a[i][j] = 1;
                }
                else if(s[j - 1] == 'v'){
                    a[i][j] = 2;
                }
                else if(s[j - 1] == '<'){
                    a[i][j] = 3;
                }
                else{
                    a[i][j] = 4;
                }
                if(s[j - 1] != '.'){
                    cnt1[i]++;
                    cnt2[j]++;
                }
            }
        }
        int flag = 1;
        for(int ii = 1; ii <= n; ++ii){
            for(int jj = 1; jj <= m; ++jj){
                int i = ii;
                int j = jj;
                if(a[i][j] != 5){
                    if(cnt1[i] == 1 && cnt2[j] == 1){
                        flag = 0;
                    }
                }
                if(a[i][j] == 3){
                    j--;
                    while(j > 0 && a[i][j] == 5) j--;
                    if(j == 0) ans ++;
                }
                else if(a[i][j] == 4){
                    j++;
                    while(j <= m && a[i][j] == 5) j++;
                    if(j == m + 1) ans ++;
                }
                else if(a[i][j] == 1){
                    i--;
                    while(i > 0 && a[i][j] == 5) i--;
                    if(i == 0) ans ++;
                }
                else if(a[i][j] == 2){
                    i++;
                    while(i <= n && a[i][j] == 5) i++;
                    if(i == n + 1) ans ++;
                }
            }
        }
        if(!flag){
            printf("Case #%d: IMPOSSIBLE\n", qw);
        }
        else{
            printf("Case #%d: %d\n", qw, ans);
        }
    }
    return 0;
}
