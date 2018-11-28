#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,ii,d,p[1005],i,j,ans,tmp;
    cin>>t;
    for(ii=1;ii<=t;ii++)
    {
        cin>>d;
        for(i=0;i<d;i++)
        {
            cin>>p[i];
        }
        ans=1000000000;
        for(i=1;i<=1000;i++)
        {
            tmp=i;
            for(j=0;j<d;j++)
            {
                if(p[j]>i)
                {
                    tmp+=p[j]/i+(p[j]%i?1:0)-1;
                }
            }
            ans=min(ans,tmp);
        }
        cout<<"Case #"<<ii<<": "<<ans<<"\n";
    }
}
