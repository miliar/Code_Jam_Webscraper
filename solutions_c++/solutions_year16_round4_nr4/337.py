#include<stdio.h>
#include<algorithm>
using namespace std;
int n, w[100][2], m;
char p[30][30];
int UF[100], Res, C[100][2], D[300];
int Find(int a){
    if(a==UF[a])return a;
    return UF[a] = Find(UF[a]);
}
void Merge(int a, int b){
    a = Find(a), b = Find(b);
    if(a!=b)UF[a] = b;
}
void Do(){
    int i, j;
    for(i=0;i<300;i++){
        D[i]=999999;
        int xx = 0, yy = 0, ss = 0;
        for(j=0;j<m;j++){
            if((1<<j)&i){
                xx += w[j][0], yy += w[j][1];
                ss += w[j][0]*w[j][1];
            }
        }
        if(xx==yy){
            D[i] = min(D[i],xx*yy-ss);
        }
        for(j=1;j<i;j++){
            if((j&i)==j)D[i] = min(D[i],D[i^j]+D[j]);
        }
    }
    printf("%d\n",Res + D[(1<<m)-1]);
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int TC, TT, i, j, k;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ", TT);
        scanf("%d",&n);
        for(i=1;i<=n;i++){
            scanf("%s",p[i]+1);
        }
        for(i=1;i<=n+n;i++)UF[i]=i;
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(p[i][j]=='1')Merge(i,n+j);
                for(k=1;k<=n;k++){
                    if(p[i][k]=='1' && p[j][k]=='1')Merge(i,j);
                    if(p[i][j]=='1' && p[i][k]=='1')Merge(j+n,k+n);
                }
            }
        }
        Res = 0;
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(p[i][j]=='0' && Find(i) == Find(n+j))Res++;
            }
        }
        for(i=1;i<=n+n;i++)C[i][0]=C[i][1]=0;
        for(i=1;i<=n;i++)C[Find(i)][0]++;
        for(i=n+1;i<=n+n;i++)C[Find(i)][1]++;
        m = 0;
        for(i=1;i<=n+n;i++){
            if(C[i][0]+C[i][1]){
                w[m][0]=C[i][0],w[m][1]=C[i][1];
                m++;
            }
        }
        Do();
    }
}
