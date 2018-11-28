#include<stdio.h>
#include<stdlib.h>


long long a,b,P,Q,g,temp;

long long gcd(long long x, long long y){
    return x%y==0?y:gcd(y,x%y);
}

int main(){
    int T,cas=1,ans,flag;
    scanf("%d",&T);
    while(T--){
        scanf("%lld/%lld",&P,&Q);
        g=gcd(P,Q);
        P/=g;
        Q/=g;
        printf("Case #%d: ",cas++);
        flag=0;
        temp=Q;
        while(1){
            if(temp%2==0)
                temp/=2;
            else if(temp==1)
                break;
            else{
                flag=1;
                break;
            }
        }
        if(flag){
            printf("impossible\n");
            continue;
        }
        ans=0;
        while(P<Q){
            P*=2;
            ans++;
        }
        printf("%d\n",ans);
    }



    return 0;
}
