#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
struct data{
    int x,wz;
}A[1005];
int D1[1005],D2[1005];
inline bool operator < (data a,data b){
    return a.x<b.x;
}
int main(){
    int T,n,m,i,j,k,l,tt=0;
    scanf("%d",&T);
    freopen("B.out","w",stdout);
    while(T--){
        scanf("%d",&n);
        for(i=1;i<=n;i++){
            scanf("%d",&A[i].x);
            A[i].wz=i;
        }
        sort(A+1,A+1+n);
        for(i=1;i<=n;i++){
            D1[i]=D2[i]=0;
            for(j=i+1;j<=n;j++)
                if(A[j].wz<A[i].wz)D1[i]++;
                else D2[i]++;
        }
        //memset(F,0xff,sizeof(F));
        //F[0]=0;
        int ans=0;
        for(i=1;i<=n;i++){
            ans+=min(D1[i],D2[i]);
        }
        tt++;
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
