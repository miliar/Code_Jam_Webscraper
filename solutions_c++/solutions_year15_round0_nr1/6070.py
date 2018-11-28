#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int t,n,co,ans,stand;
    string str;
    cin>>t;
    for(int x=0;x<t;x++)
    {
        cin>>n;
        cin>>str;
        stand=0;
        ans=0;
        for(int shy=0;shy<=n;shy++)
        {
            co=str[shy]-'0';
            if(co>0)
            {
                if(stand<shy) //people standing less than shyness level modify stand and ans
            {
                ans=ans+(shy-stand);  //called some friends
                stand=stand+co+(shy-stand);
            }
            else
                {
                    stand=stand+co;
                }
            }
        }
        cout<<"Case #"<<x+1<<": "<<ans<<"\n";
    }
    return 0;
}
