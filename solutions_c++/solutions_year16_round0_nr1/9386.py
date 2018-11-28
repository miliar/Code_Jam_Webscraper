#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<climits>
#define ll long long
using namespace std;

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    ll t,n;
    ll y=1;
    cin>>t;
    while(t--)
    {
        set<ll> s;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<y<<": ";
            cout<<"INSOMNIA"<<endl;
        }else{
            ll fg=1;
            while(s.size()!=10)
            {
                ll digit,p=n;
                p*=fg;
                while(p!=0)
                {
                    digit=p%10;
                    s.insert(digit);
                    p=p/10;
                }
                fg++;
            }
            cout<<"Case #"<<y<<": ";
            cout<<(fg-1)*n<<endl;
        }
        y++;
    }
return 0;
}
