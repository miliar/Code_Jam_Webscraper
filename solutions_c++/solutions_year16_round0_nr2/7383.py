#include <stdio.h>

char s[1000];
int TT,sum;
int main(){
    int T; scanf("%d",&T); while(T--){
        int i;

        scanf("%s",s);
        for (i=0;s[i];i++);
        int end=i;
        
        sum=0;
        for (i=end-1;i>=0;i--){
            if (((sum&1)==0 && s[i]=='-') || ((sum&1)==1 && s[i]=='+')) sum++;
        }
        printf("Case #%d: %d\n",++TT,sum);
    }
    return 0;
}




/*
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
*/
