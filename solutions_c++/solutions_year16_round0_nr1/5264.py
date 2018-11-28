#include <bits/stdc++.h>
using namespace std;
#define L long long
int main()
{
    L t,n;
    cin>>t;
    for(int I=1;I<=t;I++)
    {
        int v=0;
        cin>>n;
        bool a[10]={0};
        int i=1;
        L x;
        for(i=1;i<=100;i++)
        {
            x=n*i;
            while(x)
            {
                if(!a[x%10])
                {
                    a[x%10]=1;
                    v++;
                }
                x/=10;
            }
            if(v==10)
                break;
        }
        x=n*i;
        cout<<"Case #"<<I<<": ";
        if(v<10)
            cout<<"INSOMNIA\n";
        else
            cout<<x<<endl;
    }
}
