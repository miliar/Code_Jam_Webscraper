#include <bits/stdc++.h>
using namespace std;

#define LL long long

bool np[100001];
vector <LL> prime;
LL prime_size;
LL save[11];

void sieve()
{
    np[0] = np[1] = true;
    prime.push_back(2);
    for(LL i=4;i<=100000;i+=2) np[i] = true;
    for(LL i=3;i<=100000;i+=2)
    {
        if(!np[i])
        {
            prime.push_back(i);
            for(LL j=i*i;j<=100000;j+=(i<<1)) np[j] = true;
        }
    }
    prime_size = prime.size();
}

bool is_prime(LL n)
{
    for(LL i=0;i<prime_size  && prime[i]*prime[i] <= n;i++)
        if(n%prime[i] == 0) return false;
    return true;
}


bool convert(LL n,LL i)
{
    LL ans = 0;
    LL t = 1;
    while(n)
    {
        if(n&1) ans += t;
        t *= i;
        n /= 10;
    }
    //printf("%lld ",ans);
    if(is_prime(ans)) return false;
    save[i] = ans;
    return true;
}

bool valid(LL n)
{
    for(LL i=2;i<=10;i++)
    {
        if(!convert(n,i)) return false;
    }
    return true;
}

LL power(LL n,LL j)
{
    LL ans=1;
    for(LL i=0;i<j;i++){
        ans=ans*n;
    }
    return ans;
}

int main()
{
    freopen("out.txt", "w", stdout);
    sieve();
    char str[100];
    LL t,qq=1;
    scanf("%lld",&t);
    while(t--)
    {
        LL N,J;
        scanf("%lld %lld",&N,&J);
        printf("Case #%lld:\n",qq++);

        LL num = 1;
        for(LL i=1;i<N;i++) num = num * 10;
        num++;
        LL tmp=num;
        LL p=0;

        while(J)
        {
            LL ans=0;
            LL s=0;
            LL temp=p;
            while(temp!=0){
                ans=(temp%2)*power(10,s)+ans;
                temp/=2;
                s++;
            }

            num =tmp+ans;
            p+=2;

            if(!valid(num)) continue;
            //cout<<endl;
            LL temptmp=0;
            while(num!=0){
                str[temptmp++]=num%10+48;
                num/=10;
            }
            str[temptmp]='\0';
            for(LL i=0;i<N/2;i++) swap(str[i],str[N-i-1]);
            printf("%s",str);

            for(LL k=2;k<=10;k++)
            {
                LL n = save[k];
                //printf("%lld",n);
                for(LL i=0;i<prime_size && prime[i]*prime[i] <= n;i++)
                    if(n%prime[i] == 0) { printf(" %lld",n/prime[i]) ; break; }
            }

            J--;
            puts("");
        }
    }
    return 0;
}
