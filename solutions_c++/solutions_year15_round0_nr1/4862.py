#include<bits/stdc++.h>

using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);
    long long int i,j,t,k=0;
    long long int n,l,ans,y,x;
    string s;
    cin>>t;
    while(t--)
    {
        k++;
        ans=0;
//        scanf("%d",&n);
        cin>>n>>s;
        x=0;
        for(i=0;i<=n;i++)
        {
            if(x<i)
            {
                ans+=(i-x);
                x=i;
            }
            x+=(s[i]-48);
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
