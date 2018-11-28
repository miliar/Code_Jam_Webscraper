#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Alout.txt","w",stdout);
    long t;
    cin>>t;

    for(long i=1;i<=t;i++)
    {
        int a[10]={0};
        long count =0;
        long n;
        cin>>n;
        if(n==0)
            cout<<"Case #"<<i<<": INSOMNIA\n";
        else
        {long x=n;

        while(x>0)
        {
            int w=x%10;
            if(!a[w])
            {
                count++;a[w]=1;

            }
            x=x/10;
        }
        long y=n;

        while(count<10)
        {
            n+=y;
            x=n;
        while(x>0)
        {

            int w=x%10;
            if(!a[w])
            {
                count++;a[w]=1;
            }
            x=x/10;
        }

        }
         cout<<"Case #"<<i<<": "<<n<<"\n";
        }
    }
    return 0;
}
