#include <bits/stdc++.h>
#define  pb     push_back
#define  MAX    10000007
#define  mod    100000007
#define  read   freopen("A-large (3).in","r",stdin);
#define  write  freopen("out.txt","w",stdout);
#define  inf   (1<<30)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;



int main()
{
    //read;
    //write;
    ll test;
    scanf("%lld",&test);
    ll j=1,cnt;
    for(ll cas=1; cas<=test; cas++)
    {
        ll n;
        cnt=0,j=1;
        scanf("%lld",&n);

        bool chk[20];
        for(int i=0; i<20; i++) chk[i]=false;
        printf("Case #%lld: ",cas);
        if(n==0)
        {
            puts("INSOMNIA");
            continue;
        }
        ll temp;
        while(cnt<=10)
        {
            int k=n*j;
            temp=k;
            //  cout<<k<<endl;
            j++;
            while(k)
            {
                ll last=k%10;
                // cout<<k<<endl;
                if(chk[last]==false)
                {
                    chk[last]=true;
                    cnt++;
                }
                k/=10;
            }
            if(cnt>=10)
            {
                printf("%lld\n",temp);
                break;
            }

        }



    }


    return 0;
}
