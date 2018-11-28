#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int hash[10];
void work(int idx)
{
    printf("Case #%d: ",idx);
    int n;
    scanf("%d",&n);
    long long N=0;
    memset(hash,0,sizeof(hash));
    if (n==0)
    {
        printf("INSOMNIA\n");
        return;
    }
    int cnt=10;
    for (int i=1;i;i++)
    {
        N+=n;
        long long tmp=N;
        while(tmp>0)
        {
            int digit=tmp%10;
            if (hash[digit]==0)
            {
                hash[digit]=1;
                cnt--;
            }
            tmp/=10;
        }
        if (cnt==0)
        {
            printf("%lld\n",N);
            return;
        }
    }
}
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    work(i);
    return 0;
}
