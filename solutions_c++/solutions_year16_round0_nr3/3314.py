#include <stdio.h>
int n;
char s[20];
long long ans[15];
long long my_pow (int x,int y)
{
    long long r=1;

    for(int i=0;i<y;i++)
        r*=(long long)x;

    return r;
}
int is_prime (long long num,int dig)
{
    for(long long i=2;i*i<=num;i++){
        if(num%i==0){
            ans[dig]=i;
            return 0;
        }
    }

    return 1;
}
int is_ok (void)
{
    int i,j;
    long long t;

    for(i=2;i<=10;i++){
        t=0;
        for(j=0;j<n;j++)
            t+=s[j]*my_pow(i,j);

        if(is_prime(t,i)) return 0;
    }

    return 1;
}
void pp (void)
{
    int i=1;

    s[1]++;
    while(s[i]>1){
        s[i]=0;
        s[++i]++;
    }

    return ;
}
int main (void)
{
    int i,j,t,x,cnt=0;

    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    scanf("%d %d",&n,&x);

    s[0]=1; s[n-1]=1; s[n]='\0';
    puts("Case #1:");
    for(i=0;i<(1<<(n-2)) && cnt<x;i++,pp()){
        if(is_ok()){
            for(j=n-1;j>=0;j--) printf("%d",s[j]);
            for(j=2;j<=10;j++) printf(" %lld",ans[j]);
            printf("\n");
            cnt++;
        }
    }

    return 0;
}
