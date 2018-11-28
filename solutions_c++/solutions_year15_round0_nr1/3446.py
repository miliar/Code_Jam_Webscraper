#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<climits>
#include<stack>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    string s;
    ll tc,n,ans,tot,i,t;
    cin>>tc;
    for(t=1;t<=tc;t++)
    {
        cin>>n>>s;
        ans=0,tot=0;
        for(i=0;i<=n;i++)
        {
            if(i>tot)
            {
                ans+=(i-tot);
                tot+=((i-tot)+(s[i]-'0'));
            }
            else
            {
                tot+=(s[i]-'0');
            }
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}