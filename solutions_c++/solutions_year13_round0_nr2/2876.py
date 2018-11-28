#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int T,N,M,a[101][101],Min,Max;
bool flag,column[101],row[101];
int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>T;
    for (int kase = 1;kase <= T; kase++) {
        scanf("%d%d",&N,&M); Min = 100; Max = 1;
        for (int i = 1;i <= N; i++)
            for (int j = 1;j <= M; j++) {
                scanf("%d",&a[i][j]);
                if (Min > a[i][j]) Min = a[i][j];
                if (Max < a[i][j]) Max = a[i][j];
            }
        flag = true;
        for (int limit = Min;limit <= Max; limit++) {
            memset(column,0,sizeof(column));
            memset(row,0,sizeof(row));
            for (int i = 1;i <= N; i++) {
                int tot = 0;
                for (int j = 1;j <= M; j++) 
                    if (a[i][j] <= limit) tot++;
                if (tot == M) row[i] = true; 
            }
           for (int i = 1;i <= M; i++) {
                int tot = 0;
                for (int j = 1;j <= N; j++) 
                    if (a[j][i] <= limit) tot++;
                if (tot == N) column[i] = true; 
            }
            for (int i = 1;i <= N; i++){ 
                for (int j = 1;j <= M; j++) 
                    if ( a[i][j] <= limit && (!row[i]) && (!column[j]) ) { flag = false; break; }
            if (!flag) break;    
            }
            if (!flag) break;    
        }
        printf("Case #%d: ",kase);
        if (flag) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
