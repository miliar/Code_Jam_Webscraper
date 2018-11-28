#include <iostream>
using namespace std;
#define ll long long
int a[10];

void digit(ll n)
{   while(n)
    {   a[n%10]++;
        n/=10;
    }
}

int check()
{   for(int i=0;i<10;++i)
        if(a[i]==0)
            return 0;
    return 1;
}

int main()
{   ll x,i;
    cin>>x;
    for(i=0;i<x;++i)
    {   ll n,p;
        cin>>n;
        p=n;
        cout<<"Case #"<<i+1<<": ";
        for(int j=0;j<10;++j)
            a[j]=0;
        if(!n)
        {   cout<<"INSOMNIA\n";
            continue;
        }
        while(1)
        {   digit(n);
            if(check())
            {   cout<<n<<"\n";
                break;
            }
            n+=p;
        }
    }
    return 0;
}
