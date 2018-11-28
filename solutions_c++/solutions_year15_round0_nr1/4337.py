#include<bits/stdc++.h>
using namespace std;
// Ayush Garg
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.txt","w",stdout);

    int i,t,j,l,ct,x,ans;
    char s[1010];
    cin>>t;
    for(j=1;j<=t;j++)
    {
        ans=0;
        cin>>l>>s;
        ct=s[0]-48;
        for(i=1;i<=l;i++)
        {
            x=s[i]-48;
            if(x>0 && i>ct)
            {
                ans+=(i-ct);
                ct=i+x;
            }
            else
                ct+=x;
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }

    return 0;
}
