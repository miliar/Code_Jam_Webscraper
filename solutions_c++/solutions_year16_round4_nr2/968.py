#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int n, t;
double p[300];
double a[300];
double f[300][300];
double pick[300];
double answer;
void dfs(int x, int y){
    if (x > n){
        if (y == t+1){
            f[0][0] = 1;
            for (int i = 1; i <= t; i++){
                for (int j = 0; j <= i;j++){
                    f[i][j] = f[i-1][j] * (1 - a[i]);
                    if (j > 0){
                        f[i][j] += f[i-1][j-1] * (a[i]);
                    }
                }
            }
            double ans = f[t][t / 2];
            if (ans > answer){
                answer = ans;
                for (int i = 1; i <= t;i++){
                    pick[i] = a[i];
                }
            }
        }
        return;
    }
    a[y] = p[x];
    dfs(x+1,y+1);
    dfs(x+1,y);
}


int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    cin >> T;
    int w = 1;
    
    for (int w = 1;w<=T;w++){
        cin >> n >> t;
        for (int i = 1; i <= n; i++){
            cin >> p[i];
        }
        sort(p+1,p+n+1);
        // dfs(1,1);
        // int st = 1;
        // int en = n;
        // int select = 0;
        // while (p[st] < 0.5 && p[en] > 0.5 && select < t){
            // a[++select] = p[st];
            // a[++select] = p[en];
            // st++;en--;
        // }
        // if (!(p[st] < 0.5)){
            // while (select != t){
                // a[++select] = p[st];
                // st++;
            // }
        // }else{
            // while (select != t){
                // a[++select] = p[en];
                // en--;
            // }
        // }
        answer = 0;
        for (int tp = 0; tp <= t;tp++){
            int select = 0;
            for (int i = 1; i <= tp; i++){
                a[++select] = p[i];
            }
            for (int i = n; select != t;i--){
                a[++select] = p[i];
            }
            f[0][0] = 1;
            for (int i = 1; i <= t; i++){
                for (int j = 0; j <= i;j++){
                    f[i][j] = f[i-1][j] * (1 - a[i]);
                    if (j > 0){
                        f[i][j] += f[i-1][j-1] * (a[i]);
                    }
                }
            }
            if (f[t][t/2] > answer)
                answer = f[t][t/2];
        }
        printf("Case #%d: ", w);
        printf("%.7f\n",answer);
        // for (int i = 1; i <= t;i++){
            // printf("%.7f ",pick[i]);
        // }
        // printf("\n");
        // for (int i = 1; i <= n;i++){
            // printf("%.7f ",p[i]);
        // }
        // printf("\n");
    }
}