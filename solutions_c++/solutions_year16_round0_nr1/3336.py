#include<cstdio>
using namespace std;
long long n,answer;
int used[10],rem;
void update(long long current)
{
    long long e;
    if(current==0LL)
    {
        if(!used[0])rem--;
        used[0]=1;
    }
    while(current)
    {
        e=current%10LL;
        current/=10LL;
        if(!used[e])rem--;
        used[e]=1;
    }
}
void solve()
{
    rem=10;
    answer=1LL;
    while(rem)
    {
        update(n*answer);
        answer++;
    }
    answer--;
    answer*=n;
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%lld",&n);
        if(n==0LL)
        {
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        for(int j=0;j<10;j++)
            used[j]=0;
        solve();
        printf("Case #%d: %lld\n",i,answer);
    }
}
