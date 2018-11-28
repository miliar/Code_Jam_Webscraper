#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        int k=1,c=0,p,ans=0,m;
        string s;
        cin>>s;
        int a[s.length()];
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='+')
                a[i]=1;
            else
                a[i]=0;
        }
        while(1)
        {
            c=0;
            for(int i=0;i<s.length();i++)
            {
                if(a[i]==1)
                    c++;
            }
            if(c==s.length())
                break;
            ans++;
            for(int i=0;i<s.length();i++)
            {
                if(a[i]==0)
                    m=i;
            }
            for(int i=0;i<=m;i++)
            {
                if(a[i]==1)
                    a[i]=0;
                else
                    a[i]=1;
            }
        }
        cout<<"Case #"<<j<<":"<<" "<<ans<<endl;

    }
	return 0;
}
