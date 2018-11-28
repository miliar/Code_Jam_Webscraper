#include<stdio.h>
#include<algorithm>
#define N 110
using namespace std;
int n,m;
int a[N][N];
int rmax[N],cmax[N];
bool ok(){
    for(int i=0;i<n;i++)for(int j=0;j<m;j++){
        if(rmax[i]>a[i][j]&&cmax[j]>a[i][j])return 0;
    }
    return 1;
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)for(int j=0;j<m;j++)scanf("%d",a[i]+j);
        for(int i=0;i<n;i++){
            rmax[i]=0;
            for(int j=0;j<m;j++)rmax[i]=max(rmax[i],a[i][j]);
        }
        for(int i=0;i<m;i++){
            cmax[i]=0;
            for(int j=0;j<n;j++)cmax[i]=max(cmax[i],a[j][i]);
        }
        if(ok())printf("Case #%d: YES\n",t);
        else printf("Case #%d: NO\n",t);
    }
    return 0;
}
