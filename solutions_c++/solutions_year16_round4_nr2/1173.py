#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
double d[30],dd[30],ans;
int main(){
    int tc;
    freopen("B-small-attempt3.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        ans=0.0;
        int n,k;
        scanf("%d %d",&n,&k);
        for(int i=0;i<n;i++){
            scanf("%lf",&d[i]);
        }
        int xx=pow(2,n);
        for(int i=0;i<xx;i++){
            int num=0;
            for(int j=0;j<n;j++){
                if((i&(1<<j))!=0){
                    dd[num]=d[j];
                    num++;
                }
            }
//            printf("%d %d\n",i,num);
            if(num!=k)  continue;
//            printf("*%d*",i);
            int xyz=pow(2,k);
//            printf("%d",xyz);
            int num2=0;
            double sm=0.0;
            for(int j=0;j<xyz;j++){
                num2=0;
                for(int l=0;l<num;l++){
                    if((j&(1<<l))!=0){
                        num2++;
                    }
                }
//                printf("*%d %d ",j,num2);
                if(num2!=k/2){
                    continue;
                }
                double q1=1.0;
                for(int l=0;l<num;l++){
                    if((j&(1<<l))!=0){
                        q1*=dd[l];
                    }
                    else{
                        q1*=1-dd[l];
                    }
                }
//                printf(" %f*\n",q1);
                sm+=q1;
            }
            ans=max(ans,sm);
        }
        printf("Case #%d: %.8f\n",t,ans);
    }
}
