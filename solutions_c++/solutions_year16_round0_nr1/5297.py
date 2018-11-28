#include <bits/stdc++.h>

using namespace std;
#define ll long long int
set <int> st;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    ll t;
    cin>>t;
    ll n;
    for(int tt=1;tt<=t;tt++)
    {

        cin>>n;
        if(n==0)
           cout<<"Case #"<<tt<<": INSOMNIA"<<endl;
        else
        {
            ll x=n;
            while(x>0)
            {
               int tmp=x%10;
                st.insert(tmp);
                x=x/10;
            }
            x=n;
            ll pro,yaad;
            int fl=0;
           // cout<<st.size()<<endl;
            for(ll i=2;i<=100;i++)
            {
               pro=x*i;
                yaad=pro;
               while(pro>0)
               {
                int tmp=pro%10;
                st.insert(tmp);
                if(st.size()==10)
                {
                    fl=1;
                    break;
                }
                pro=pro/10;
               }
               if(fl==1)
               {
                   break;
               }
            }
            if(fl==0)
                cout<<"Case #"<<tt<<": INSOMNIA"<<endl;
            else
                cout<<"Case #"<<tt<<": "<<yaad<<endl;
            st.clear();
        }
    }


}
