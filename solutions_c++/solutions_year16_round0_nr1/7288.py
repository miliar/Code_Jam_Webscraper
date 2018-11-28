#include <stdio.h>

int chk[10],cnt;
long long int n;
int solve(long long int a){
    while(a){
        if (!chk[a%10]) cnt++;
        chk[a%10]=1;
        a/=10;
        if (cnt==10) return 1;
    }
    return 0;
}

int main(){
    int TT=1;
    int T; scanf("%d",&T); while(T--){

        printf("Case #%d: ",TT++);
        
        long long int i; cnt=0;
        scanf("%lld",&n);
        
        if (n==0){
            printf("INSOMNIA\n");
            continue;
        }
        for (i=0;i<10;i++) chk[i]=0;
        for (i=1;;i++)
            if (solve(i*n)) break;
        printf("%lld\n",i*n);
    }
    return 0;
}
