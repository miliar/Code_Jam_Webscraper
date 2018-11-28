#include<bits/stdc++.h>
using namespace std;
int hsh[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("countingsheep_output.txt","w",stdout);
    int t,ct,nub=1;
    long long n,keb,i;
    scanf("%d",&t);
    while(t--)
    {
        memset(hsh,0,sizeof hsh);
        scanf("%lld",&n);
        ct=0;
        for(i=1;i<=100000000;i++)
        {
            keb=i*n;
            while(keb!=0)
            {
                ct+=1-hsh[keb%10];
                hsh[keb%10]=1;
                keb/=10;
            }
            if(ct==10)
                break;
        }
        printf("Case #%d: ",nub++);
        if(ct==10)
            printf("%lld\n",n*i);
        else
            printf("INSOMNIA\n");
    }
}
