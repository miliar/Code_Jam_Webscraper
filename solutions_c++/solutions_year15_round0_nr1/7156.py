#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int smax;
    string s;
    int g=1;
    while(t--)
    {
        cin>>smax>>s;
        int ans = 0;
        int cnt=0;
        for(int i=0;i<=smax;i++)
        {
            if(cnt<i && s[i]!='0')
            {
                ans+=(i-cnt);
                cnt = i;
            }
            cnt+=(s[i]-48);
        }
        cout<<"Case #"<<g<<": "<<ans<<"\n";
        g++;
    }
    return 0;
}
