#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("codejam2015large.out", "wt", stdout);
    int k,t,ans,i,j,S,mx;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int a[2000],b[2000];
        memset(b,0,sizeof(b));
        ans=0;
        mx=0;
        string s;
        cin>>S>>s;
        for(i=0;i<s.size();i++)
            a[i]=s[i]-'0';

        for(i=0;i<S;i++)
        {
            b[i+1]=b[i]+a[i];
        }

        /*for(i=0;i<=S;i++)
            cout<<b[i]<<" ";
        cout<<endl;*/

        for(i=0;i<=S;i++)
        {
            if(b[i]>=i)
                continue;
            else
            {
                mx=max(mx,i-b[i]);
            }
        }
        printf("Case #%d: %d\n",k,mx);
    }
    return 0;
}
