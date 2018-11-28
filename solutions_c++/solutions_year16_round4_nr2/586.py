#include<bits/stdc++.h>
using namespace std;

const int N=220;
long double dp[N][N<<1];
double a[N],b[N];

const double eps=1e-13;
const double dcmp(double x){
    if(fabs(x)<eps)return 0;
    return x<0?-1:1;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for(int _=1;_<=test;_++){
        int n,K;
        scanf("%d%d",&n,&K);
        for(int i=0;i<n;i++){
            scanf("%lf",&a[i]);
        }
        sort(a,a+n);

        double ret=0;
        for(int mm=0;mm<=K;mm++){
            int cc=0;
            for(int i=0; i<mm; i++)
            {
                b[cc++]=a[i];
            }
            for(int i=0;i<K-mm;i++){
                b[cc++]=a[n-1-i];
            }

            memset(dp,0,sizeof(dp));
            dp[0][N]=1;
            for(int i=0; i<K; i++)
            {
                for(int j=0; j<2*N; j++)
                {
                    if(dcmp(dp[i][j])<=0)continue;
                    dp[i+1][j+1]+=dp[i][j]*b[i];
                    dp[i+1][j-1]+=dp[i][j]*(1-b[i]);
                }
            }
            ret=max(ret,(double)dp[K][N]);
        }

        printf("Case #%d: %.10f\n",_,ret);
    }
    return 0;
}
