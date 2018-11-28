#include<bits/stdc++.h>
using namespace std;
int a[20];
bool f(long long n)
{
    long long x,i;
    while(n>0)
    {
        x=n%10;

       // cout<<x<<endl;
        a[x]=1;
        n/=10;
    }
    for(i=0;i<=9;i++)
    {
       // cout<<a[i]<<" ";
        if(a[i]==0)
            return 0;
    }
    //cout<<endl;
    return 1;
}
int main()
{

   // cout<<f(1234567890);
    //freopen("A-large (1).in","r",stdin);
    //freopen("out.txt","w",stdout);
    long long t,n,chk,iner,i,x;
    cin>>t;
    for(iner=1;iner<=t;iner++)
    {
        printf("Case #%lld: ",iner);
        cin>>n;
        x=n;
        memset(a,0,sizeof(a));
        chk=0;
        for(i=1;i<=100000;i++)
        {
            n=x*i;
            //cout<<n<<endl;
            bool c=f(n);
            if(c)
            {
                cout<<n;
                chk=1;
                break;
            }
            else
            {
               // n=x*i;
                if(n>1000000000000)
                {
                    break;
                }
            }

        }
        if(!chk)
            cout<<"INSOMNIA";
    cout<<endl;
    }
}
