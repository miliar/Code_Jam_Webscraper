#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
int A[10][10],B[10][10];
int N;
char ch[20][20];
int used[10],uk[10];
bool dfs(int n) {
    if(n==N) return true;
    for(int i=0;i<N;i++) {
        if(used[i] == 0) {
            used[i] = 1;
            bool jud = false;
            for(int j=0;j<N;j++) {
                if(uk[j] == 0 && B[i][j] > 0) {
                    uk[j] = 1;
                    if(dfs(n+1) == false) {
                        jud = false;
                        break;
                    }
                    else jud = true;
                    uk[j] = 0;
                }
            }
            if(jud == false) return false;
            used[i] = 0;
        }
    }
    return true;
}
int main(){
    freopen("di.in","r",stdin);
   freopen("do.out","w",stdout);
    int T;scanf("%d",&T);
    for(int tt=1;tt<=T;tt++){
        scanf("%d",&N);
        for(int i=0;i<N;i++) {
            scanf("%s",ch[i]);
            for(int j=0;j<N;j++) {
                if(ch[i][j] == '0') A[i][j] = 0;
                else A[i][j] = 1;
            }
        }
        int ans = N*N;
        for(int n=0;n<(1<<(N*N));n++) {
            int s = 0;
            for(int i=0;i<N;i++) for(int j=0;j<N;j++) B[i][j] = A[i][j];
            for(int i=0;i<N*N;i++) {
                if(n&(1<<i)) {
                    s++;
                    B[i/N][i%N] = 1;
                }
            }
            memset(used,0,sizeof(used));
            memset(uk,0,sizeof(uk));
            if(dfs(0)) ans = min(ans,s);
        }
        printf("Case #%d: %d\n",tt,ans);
    }
}
