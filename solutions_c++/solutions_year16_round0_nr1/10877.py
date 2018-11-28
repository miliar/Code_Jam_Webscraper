#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    freopen("i.txt", "r", stdin);
    freopen("o.txt", "w", stdout);
    ll t;
    cin>>t;
    for(ll i=1 ; i<=t ; i++)
    {
        ll n , counter=2;
        cin>>n;
        if(!n)
           {
               cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
               continue;
           }
        set<ll>s;
        ll temp=n;
        while(1==1)
        {
            bool flag=0;
            ll temp1=temp;
            while(temp1)
            {
                s.insert(temp1%10);
               /* for(auto it : s)
                    cout<<it<<" ";
                cout<<endl;*/
                if(s.size()==10)
                {
                    flag=1;
                    cout<<"Case #"<<i<<": "<<temp<<endl;
                    break;
                }
                temp1/=10;
            }
            if(flag)
                break;
            else
               {
                   temp=n;
                   temp*=counter++;
               }
        }
    }

    return 0;
}
