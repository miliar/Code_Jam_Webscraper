#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){

    int T,D,i,j,k,P[1000],res,minn;
    scanf("%d",&T);
    for(i=0;i<T;i++){
        scanf("%d",&D);
        for(j=0;j<D;j++) scanf("%d",&P[j]);
        sort(P,P+D);
        minn=0x5fffffff;
        for(j=P[D-1];j>=1;j--){
            res=0;
            for(k=D-1;k>=0;k--){
                if(P[k]<j) break;
                else{
                    if(P[k]%j==0) res+=(P[k]/j)-1;
                    else res+=(P[k]/j);
                }
            }
            if(minn>res+j) minn=res+j;
        }
        printf("Case #%d: %d\n",i+1,minn);
    }
}
