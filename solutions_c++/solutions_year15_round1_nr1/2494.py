#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,i,tt,ans1,ans2,n,maxdiff;
    int a[1005];
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        ans1=ans2=maxdiff=0;
        memset(a,0,sizeof(a));
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            if(i!=0)
            {
                maxdiff=max(maxdiff,a[i-1]-a[i]);
                if(a[i-1]>a[i])ans1+=(a[i-1]-a[i]);
            }
        }
        for(i=0;i<n-1;i++)
        {
            ans2+=min(a[i],maxdiff);
        }
        cout<<"Case #"<<tt<<": "<<ans1<<' '<<ans2<<"\n";
    }
    return 0;
}
