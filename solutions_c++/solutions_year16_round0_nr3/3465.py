#include<stdio.h>
long long isPrime(long long num)
{
    if(num!=2 && num%2==0) return 2;
    for(long long i=3; i*i<=num; i+=2)
    {
        if(num%i==0) return i;
    }
    return 0;
}
int main()
{
    long long i, j, tmp, s, T, n, k, x, arr[11], cnt=0;
    scanf("%lld", &T);
    for(long long tt=1; tt<=T; ++tt)
    {
        scanf("%lld%lld", &n, &k);
        printf("Case #%lld:\n", tt);
        for(i=(1<<(n-1))+1; i<(1<<n)-1 && cnt<k; i+=2)
        {
            for(j=2; j<=10; ++j)
            {
                s=0;tmp=i;x=1;
                while(tmp)
                {
                    s+=(tmp%2)*x;
                    x*=j;
                    tmp/=2;
                }
                x=isPrime(s);
                if(x==0) break;
                arr[j]=x;
            }
            if(j<=10) continue;
            printf("%lld", s);
            for(j=2; j<=10; ++j) printf(" %lld", arr[j]);
            printf("\n");
            ++cnt;
        }
    }
}