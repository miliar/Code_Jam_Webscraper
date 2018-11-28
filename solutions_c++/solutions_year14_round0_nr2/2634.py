#include <stdio.h>
int main(){
    freopen("c1.in","r",stdin);
    freopen("c1.out","w",stdout);
    double c,f,x,cur,sum,s,ans;
    int t,flag;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%lf%lf%lf",&c,&f,&x);
        ans=x;flag=1;s=2;cur=0;
        while(flag){
            sum=x/s+cur;
            cur=c/s+cur;
            s=s+f;
            if(ans>sum)
                ans=sum;
            else
                flag=0;
        }
        printf("Case #%d: %.7lf\n",i,ans);
    }
    return 0;
}
