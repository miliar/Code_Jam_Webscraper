#include<iostream>
using namespace std;
int main()
{
    int j,k;
    int t,ca = 1;
    long long n,i;
    cin>>t;
    while(t--)
    {
        cin>>n;
        cout<<"Case #"<<ca<<": ";
        ca++;
        if(n==0)
        {
            cout<<"INSOMNIA\n";
            continue;
        }
        int now=0;
        int ans=(1<<10)-1;
        for(i=1;i<1000000;i++)
        {
            long long x = n * i;
            while(x!=0)
            {
                now |= (1<<(x%10));
                x/=10;
            }
            if(now==ans)
            {
                cout<<n*i<<endl;
                break;
            }
        }
        if(now!=ans)
        {
            cout<<"INSOMNIA\n";
        }
    }
}

