#include <bits/stdc++.h>
using namespace std;
#define ll long long

int a[10];
ll arr[1000001];

int solve(ll x)
{
    while(x)
    {
        int in = x%10;
        x /= 10;
        a[in] = 1;
    }
    for(int i=0;i<10;i++)
    {
        if(!a[i])
        return 0;
    }
    return 1;
}

void insomnia()
{
    for(ll i=1;i<1000001;i++)
    {
        memset(a,0,sizeof(a));
        ll j = 1;
        while(!solve(j*i))
        j++;
        arr[i] = i*j;
    }
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    insomnia();
    scanf("%d",&t);
    int num = t;
    while(t--)
    {
        ll x;
        scanf("%lld",&x);
        if(x==0)
        printf("Case #%d: INSOMNIA\n",num-t);
        else
        printf("Case #%d: %lld\n",num-t,arr[x]);
    }
    return 0;
}

