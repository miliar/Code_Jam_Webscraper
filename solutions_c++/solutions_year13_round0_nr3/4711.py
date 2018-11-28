#include<cstdio>

long long a[1000007];
int s[105];
bool check(long long p)
{
    int j=0;
    while (p>0)
    {
        s[j]=p%10ll;
        p/=10ll;
        j++;
    }
    for (int i=0;i<j;i++)
        if (s[i]!=s[j-1-i]) return false;
    return true;
}
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int tmp=0;
    for (long long i=1;i<=10000000;i++)
    {
        if (!check(i)) continue;
        long long now=i*i;
        if (check(now)) a[tmp++]=now;
    }
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        long long A,B;
        scanf("%lld%lld",&A,&B);
        int ans=0;
        for (int i=0;i<tmp;i++)
            if(a[i]>=A && a[i]<=B) ans++;
        printf("Case #%d: %d\n",cas,ans);
    }
}
