#include<iostream>
#include<cstdio>
using namespace std;
typedef long long int ll;

ll brute(ll n){
    int hash[10]={0};
    ll tmp,k=0;
    int idx=0;
    while(idx!=10){
        ++k;
        tmp=n*k;
        while(tmp && idx<10){
            int x=tmp%10;
            if(!hash[x])
                ++idx;
            hash[x]=1;
            tmp/=10;
        }
        
    }
    return n*k;
}
int main(){
    ll t,n,i;
    scanf("%lld",&t);
    for(i=1;i<=t;++i){
        scanf("%lld",&n);
        if(n==0)
        {
           printf("Case #%lld: INSOMNIA\n",i);
           continue;
        }
        printf("Case #%lld: %lld\n",i,brute(n));
            
    }
    return 0;
}
