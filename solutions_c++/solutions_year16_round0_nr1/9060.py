#include<iostream>
#define ll long long
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    ll int i,x,n,temp,m;
    cin>>t;
    int a[10],f=0;
    for(i=0;i<10;i++)
        a[i]=0;
    x=0;
    while(t--)
    {
        f=0;
        x++;
        cin>>n;
        temp=n;
        m=2;

        if(n==0)
            cout<<"Case #"<<x<<": INSOMNIA"<<endl;
        if(n!=0)
        {
            while(f<10)
            {
            while(n>0)
            {

                if(a[n%10]==0)
                    {f++;
                    a[n%10]++;}
                n/=10;

            }
                n=m*temp;
                m++;
                // cout<<n<<' ';
            }
            cout<<"Case #"<<x<<": "<<(m-2)*temp<<endl;
        }
        for(i=0;i<10;i++)
            a[i]=0;
    }
    return 0;
}
