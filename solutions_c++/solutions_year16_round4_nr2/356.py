#include<stdio.h>
#include<algorithm>
using namespace std;
double w[210], P[210][210];
int n, K;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int TC, TT, i, j, cnt, tt;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ", TT);
        scanf("%d%d",&n,&K);
        for(i=1;i<=n;i++)scanf("%lf",&w[i]);
        sort(w+1,w+n+1);
        double Res = 0.0;
        for(tt=0;tt<=K;tt++){
            for(i=0;i<=n+1;i++)for(j=0;j<=n+1;j++)P[i][j]=0.0;
            P[0][0] = 1.0;
            cnt = 0;
            for(i=1;i<=n;i++){
                if(i > tt && n - (K-tt) + 1 > i)continue;
                cnt++;
                for(j=0;j<=cnt;j++){
                    P[cnt][j] = P[cnt-1][j]*(1.0-w[i]);
                    if(j)P[cnt][j] += P[cnt-1][j-1]*w[i];
                }
            }
            Res = max(Res,P[cnt][K/2]);
        }
        printf("%.11lf\n",Res);
    }
}
