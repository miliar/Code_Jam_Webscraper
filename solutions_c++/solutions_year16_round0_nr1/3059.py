#include <bits/stdc++.h>

using namespace std;
bool digits[11];
bool mark(long long n)
{
    while(n>0)
    {
        digits[n%10]=true;
        n/=10;
    }
    for(int i=0;i<10;i++)
        if(!digits[i])return false;
    return true;
}
int main()
{
    int t;
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&t);
    int curCase=1;
    while(t--)
    {
        long long n;
        for(int i=0;i<10;i++)digits[i]=false;
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",curCase);
            curCase++;
            continue;
        }
        long long num=n;
        int sol=1;
        while(!mark(num))
        {
            num+=n;
            sol++;
        }

        printf("Case #%d: %lld\n",curCase,num);
        curCase++;
    }
    return 0;
}
