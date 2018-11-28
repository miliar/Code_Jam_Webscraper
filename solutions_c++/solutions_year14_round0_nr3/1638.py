#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;
const LL INF=1ll<<60, MaxN=1<<21;
const LD eps=1e-8;

int n,m;
int a[100][100];
int R,C,M;

void writeit(){
    for (int i=0; i<R; i++){
        for (int j=0; j<C; j++)
            if (i==0 && j==0) printf("c");
            else
            if (a[i][j]==0) printf("*");
            else printf(".");
        puts("");
    }
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while (t--){
        printf("Case #%d:\n",++cas);
        scanf("%d%d%d",&R,&C,&M);
        memset(a,0,sizeof(a));
        int left=R*C-M;
        if (M==0) { memset(a,1,sizeof(a)); writeit(); continue; }
        if (left==1){ writeit(); continue; }
        if (R==1){
            for (int i=0; i<left; i++) a[0][i]=1;
            writeit(); continue;
        }
        if (C==1){
            for (int i=0; i<left; i++) a[i][0]=1;
            writeit(); continue;
        }
        if (left<4){ puts("Impossible"); continue; }
        if (R==2){
            if (M%2==1){ puts("Impossible"); continue; }
            for (int i=0; i<left/2; i++){
                a[0][i]=1; a[1][i]=1;
            }
            writeit(); continue;
        }
        if (C==2){
            if (M%2==1){ puts("Impossible"); continue; }
            for (int i=0; i<left/2; i++){
                a[i][0]=1; a[i][1]=1;
            }
            writeit(); continue;
        }
        if (left<9 && left%2==1){ puts("Impossible"); continue; }
        if (left%2==1){
            for (int i=0; i<3; i++)
                for (int j=0; j<3; j++) a[i][j]=1;
            left-=9;
            for (int i=3; i<R && left>0; i++){
                a[i][0]=1; a[i][1]=1; left-=2;
            }
            for (int i=3; i<C && left>0; i++){
                a[0][i]=1; a[1][i]=1; left-=2;
            }
            for (int j=0; j<C && left>0; j++){
                for (int i=0; i<R && left>0; i++){
                    if (a[i][j]==0){ left--; a[i][j]=1; }
                }
            }
            writeit(); continue;
        }
        else{
            for (int i=0; i<R && left>0; i++){
                a[i][0]=1; a[i][1]=1; left-=2;
            }
            for (int i=2; i<C && left>0; i++){
                a[0][i]=1; a[1][i]=1; left-=2;
            }
            for (int j=0; j<C && left>0; j++){
                for (int i=0; i<R && left>0; i++){
                    if (a[i][j]==0){ left--; a[i][j]=1; }
                }
            }
            writeit(); continue;
        }
    }
    return 0;
}
