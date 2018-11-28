/********************************************************************/
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    ll cases;
    cin>>cases;
    int t =0;
    while(cases--)
    {
        t++;
        ll num;
        cin>>num;
        string str;
        cin>>str;
        ll cp = 0;
        ll ans = 0;
        for(ll i =0;i<str.size();i++)
        {
            if(i>cp)
            {
                ll adf = (i-cp);
                ans+=adf;
                cp+=adf;
            }
            cp+=(str[i]-'0');
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
