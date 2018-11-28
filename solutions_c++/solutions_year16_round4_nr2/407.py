#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<vector>
#include<set>
#include<stack>
#include<map>
#include<ctime>
#include<bitset>
#define LL long long
#define db double
#define EPS 1e-8
#define inf 1e9

using namespace std;

long double p[300],nima1[300][300],nima2[300][300];
int k;
int main(){
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T,cas=1;
    scanf("%d",&T);
    while (T--){
        int n;
        scanf("%d%d",&n,&k);
        for (int i=0;i<n;i++){
            cin>>p[i];
        }
        long double ans=0;
        sort(p,p+n);
        for (int i=0;i<=n;i++)
            for (int j=0;j<=n;j++)
                nima1[i][j]=nima2[i][j]=0;
        nima1[0][0]=1;
        nima1[0][1]=0;
        for (int i=1; i<=n;i++){
            for (int j=0;j<=i+1;j++){
                nima1[i][j]=nima1[i-1][j]*(1-p[i-1])+nima1[i-1][j-1]*p[i-1];
            }
        }

        nima2[0][0]=1;
        nima2[0][1]=0;
        for (int i=1;i<=n;i++){
            for (int j=0;j<=i+1;j++){
                nima2[i][j]=nima2[i-1][j]*(1-p[n-i])+nima2[i-1][j-1]*p[n- i];
            }
        }

        for (int i=0;i<=k;i++) {
            long double *L=nima1[i], *R=nima2[k-i], quanzhi=0;
            for (int j=0;j<=(k/2);j++)
                quanzhi+=L[j]*R[(k/2)-j];
            if (ans<quanzhi)
                ans=quanzhi;
        }
        printf("Case #%d: %f\n",cas++,(double)ans);
    }
    return 0;
}
