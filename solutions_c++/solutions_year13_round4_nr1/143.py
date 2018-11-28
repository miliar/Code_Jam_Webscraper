#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#define Mo 1000002013
using namespace std;
struct data{
    int fl;
    long long x,y;
}A[2005];
inline bool operator < (data a,data b){
    return a.x<b.x||(a.x==b.x&&a.fl<b.fl);
}
long long lss[2005];
long long B[2005];
int main(){
    int T,n,m,i,j,k,l,tt=0;
freopen("A.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&n,&m);
        int gs=0;
        long long ans=0,ans1=0;
        tt++;
        for(i=1;i<=m;i++){
            int L,R,x;
            scanf("%d%d%d",&L,&R,&x);
            lss[++gs]=L;
            A[gs].fl=0;
            A[gs].x=L;
            A[gs].y=x;
            lss[++gs]=R;
            A[gs].fl=1;
            A[gs].x=R;
            A[gs].y=x;
            ans=(ans+(((long long)n+((long long)n-(((long long)R)-L)+1))*(((long long)R)-L)/2)%Mo*x)%Mo;
        }
        sort(A+1,A+1+gs);
        sort(lss+1,lss+1+gs);
        j=1;
        for(i=2;i<=gs;i++)
            if(lss[i]!=lss[j])lss[++j]=lss[i];
        int Gs=j;
        for(i=1;i<=gs;i++){
            A[i].x=lower_bound(lss+1,lss+1+Gs,A[i].x)-lss;
            if(!A[i].fl){
                B[A[i].x]+=A[i].y;
            }else{
                for(j=A[i].x;j>=1;j--)
                    if(A[i].y>0){
                        long long tt=0;
                        if(B[j]>=A[i].y){
                            B[j]-=A[i].y;
                            tt=A[i].y;A[i].y=0;
                        }else if(B[j]>0){
                            tt=B[j];
                            A[i].y-=B[j];
                            B[j]=0;
                        }
                        ans1=(ans1+(((long long)n+(n-(lss[A[i].x]-lss[j])+1))*(lss[A[i].x]-lss[j])/2)%Mo*tt)%Mo;
                    }else break;
            }
        }
        printf("Case #%d: %I64d\n",tt,((ans-ans1)%Mo+Mo)%Mo);
    }
    return 0;
}
