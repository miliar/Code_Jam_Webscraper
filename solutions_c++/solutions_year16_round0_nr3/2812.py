#include<bits/stdc++.h>
using namespace std;
vector<long long> prime;
bool chk[100000005];
long long a[11];
long long ch(long long x,long long b)
{
    long long multi=1,ss=0;
    while(x!=0)
    {
        ss+=(x%10)*multi;
        multi*=b;
        x/=10;
    }
    return ss;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("coinjamsmall_output.txt","w",stdout);
    long long n,now,multi,ss,t,i,j,k,ct=0,ok,ook,keb,nub=1;
    for(i=2;i<=1000000;i++)
    {
        if(!chk[i])
            prime.push_back(i);
        for(j=i+i;j<=1000000;j+=i)
            chk[j]=1;
    }
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld%lld",&n,&k);
        printf("Case #%lld:\n",nub++);
        multi=1;
        for(i=0;i<n-1;i++)
            multi*=10;
        now=multi+1;
        while(ct<k)
        {
            ok=1;
            for(i=2;i<=10;i++)
            {
                ook=0;
                ss=ch(now,i);
                for(j=0;j<prime.size();j++)
                {
                    if(prime[j]>(int)sqrt(ss))
                        break;
                    if(ss%prime[j]==0)
                    {
                        a[i]=prime[j];
                        ook=1;
                        break;
                    }
                }
                if(!ook)
                {
                    ok=0;
                    break;
                }
            }
            if(ok)
            {
                ct++;
                printf("%lld ",now);
                for(i=2;i<=10;i++)
                    printf("%lld ",a[i]);
                printf("\n");
            }
            keb=now;
            keb/=10;
            multi=10;
            while(keb!=0)
            {
                if(keb%10==0)
                    break;
                now-=multi;
                keb/=10;
                multi*=10;
            }
            now+=multi;
        }
    }
}
