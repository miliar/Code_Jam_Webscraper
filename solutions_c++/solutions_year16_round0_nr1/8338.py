#include<bits/stdc++.h>
#define ll long long
#define pf printf
#define sc scanf
using namespace std;

ll a[10]={0};

void callme(ll n)
{
    while(n>0)
    {
        a[n%10]=1;
        n/=10;
    }
}


bool check()
{
   ll cnt=0;
   for(ll i=0;i<10;i++)
   {
       if(a[i]==1)
        cnt++;
   }
   if(cnt==10)
    return true;
   return false;
}


int main()
{
     freopen("A-large.in","r",stdin);
     freopen("A.out","w",stdout);

    ll t,n,cnt,in,temp;
    cin>>t;
    for(ll i=1;i<=t;i++)
    {
        cnt=0;
        for(ll j=0;j<10;j++)
            a[j]=0;
        cin>>temp;
        pf("Case #%lld: ",i);
        in=0;

             if(temp==0)
             {
                 cout<<"INSOMNIA"<<endl;
                 continue;

             }

        while(check()!=true)
        {
            in++;
            cnt++;
            n=temp*in;


            callme(n);


        }

        cout<<n<<endl;

    }

return 0;
}
