#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#define LL long long
LL t[40],n,j,ans[15];
LL is_prime(LL a,LL x){
    LL i,s;
    s=sqrt(x);
    if(x%2==0){
        ans[a]=2;
        return 0;
    }
    for(i=3;i<=s;i+=2){
        if(x%i==0){
            ans[a]=i;
            return 0;
        }
    }
    return 1;
}
void is_ok(){
    LL x,y,z,i;
    for(i=2;i<=10;i++){
        z=n;
        y=1;
        x=0;
        while(z>0){
            x+=y*t[z];
            y*=i;
            z--;
        }
        if(is_prime(i,x)==1)   break;
    }
    if(i!=11)   return;
    printf("%lld ",x);
    for(i=2;i<=10;i++)  printf("%lld ",ans[i]);
    printf("\n");
    j--;
    if(j==0)    exit(0);
}
void f(LL cnt){
    if(cnt>=n){
        is_ok();
        return;
    }
    t[cnt]=0;
    f(cnt+1);
    t[cnt]=1;
    f(cnt+1);
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%*lld");
    scanf("%lld %lld",&n,&j);
    printf("Case #1:\n");
    t[1]=t[n]=1;
    f(2);
    return 0;
}
