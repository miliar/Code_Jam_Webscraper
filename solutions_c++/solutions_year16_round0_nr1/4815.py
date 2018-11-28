#include <iostream>
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
using namespace std;
int main()
{
    //FILE *f=freopen("test.in","rt",stdin);
    //FILE *f1=freopen("test.ou","wt",stdout);
    ll t,n;
    cin>>t;
    for (int c=0;c<t;c++)
    {
        cin>>n;
        ll value=0,cou=0;
        bool fr[10]={false};
        cout<<"Case #"<<c+1<<": ";
        if (n==0) cout<<"INSOMNIA"<<endl;
        for (int i=1;i<=1000;i++)
        {
            value+=n;
            ll value1=value;
            while (value1!=0)
            {
                if (!fr[value1%10]) cou++;
                fr[value1%10]=true;
                value1/=10;
            }
            if (cou==10)
            {
                cout<<value<<endl;
                break;
            }
        }
    }
    return 0;
}
