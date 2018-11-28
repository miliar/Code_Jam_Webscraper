#include<bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,tt;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        int s,i,j=0,ans=0;
        char st[1002];
        cin>>s;
        cin>>st;
        for(i=0;i<=s;i++)
        {
            while(j<i)
            {
                ans++;
                j++;
            }
            j=j+st[i]-'0';
        }
        cout<<"Case #"<<tt<<": "<<ans<<"\n";
    }
    return 0;
}
