#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output1-2.txt","w",stdout);
    int t,n;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        string S;
        cin>>n;
        cin>>S;
        int cum=0,ans=0;
        for(int i=0;i<=n;i++)
        {
            if(cum<i)
            {
                ans=ans+i-cum;
                cum=i;
            }
            cum=cum+S[i]-'0';
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
