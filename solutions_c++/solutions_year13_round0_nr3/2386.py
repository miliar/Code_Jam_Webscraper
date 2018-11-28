#include<stdio.h>
const char inf[]="C-large-1.in";
const char ouf[]="C-large-1.out";
const int maxn = 10000000;
const int maxcnt = 10000;

int check(long long x){
    long long p,q;
    q=0;
    for(p=x;p;p/=10){
        q=q*10+p%10;
    }
    if(q==x)
        return 1;
    return 0;
}

long long list[maxcnt+1],cnt;

void prepare(){
    long long i;
    cnt=0;
    for(i=1;i<=maxn;i++){
        if(check(i) && check(i*i))
            list[++cnt]=i*i;
    }
}

int main(){
    prepare();
    freopen(inf,"r",stdin);
    freopen(ouf,"w",stdout);
    int T,totT,i,ans;
    long long A,B;
    scanf("%ld",&totT);
    for(T=1;T<=totT;T++){
	scanf("%I64d%I64d",&A,&B);
	ans=0;
	for(i=1;i<=cnt;i++){
            if(list[i]>=A && list[i]<=B)
                ans++;
        }
	printf("Case #%ld: %ld\n",T,ans);
    }
    return 0;
}
