#include "stdio.h"
bool found[10]={};
bool check();
void update(long long x);
int main(){
    freopen("A-large.in","r",stdin);
    freopen("solution.txt","w",stdout);
    long long t,n;
    scanf("%lld",&t);
    for(long long l=1;l<=t;l++){
        scanf("%lld",&n);
        if(n==0){
            printf("Case #%lld: INSOMNIA\n",l);
            continue;
        }
        long long temp=0;
        for(long long i=0;i<10;i++) found[i]=false;
        while(!check()){
            temp+=n;
            update(temp);
        }
        printf("Case #%lld: %lld\n",l,temp);
    }
}
bool check(){
    bool check=true;
    for(long long i=0;i<10;i++) check=check&&found[i];
    return check;
}
void update(long long x){
    while(x!=0){
        found[x%10]=true;
        x/=10;
    }
}
