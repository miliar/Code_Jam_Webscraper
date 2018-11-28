#include <bits/stdc++.h>

#define ll long long
using namespace std;
bool ara[12];
int counter;

void make(ll n)
{
    while(n)
    {
        ll r = n%10;
        if(ara[r]==0)
        {
            ara[r]=1;
            counter++;
        }
        n=n/10;
    }
    return;
}
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,cases=0;
    scanf("%d",&t);

    while(t--)
    {
        memset(ara,0,sizeof(ara));
        counter=0;
        ll n,num;
        scanf("%lld",&n);

        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",++cases);
            continue;
        }
        num=n;
        do
        {
            make(num);
            if(counter==10)break;

            num+=n;
        }while(counter<10);

        printf("Case #%d: %lld\n",++cases,num);


    }
    return 0;
}
