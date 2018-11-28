#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    //freopen("Ainput.txt","r",stdin);
    //freopen("Aoutput.txt","w",stdout);
    set<ll>mp;
    ll t,n,i,it,m,no=0;
    cin>>t;
    while(t--)
    {
        cin>>n;it=0;
            //cout<<"   "<<n<<endl;
            m=n;
        while(mp.size()!=10&&it<100)
        {
            //cout<<"   "<<n<<endl;
            while(n)
            {
                mp.insert(n%10);
                n/=10;
            }
            it++;
            n=m*it;
        }
        if(mp.size()==10)
        cout<<"Case #"<<++no<<": "<<n-m<<endl;
        else cout<<"Case #"<<++no<<": "<<"INSOMNIA"<<endl;
        mp.clear();
    }
}
