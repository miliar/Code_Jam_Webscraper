#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long t;
    cin>>t;
    char str[1009];
    for(int x=0;x<t;x++)
    {
        long long cnt=0,ans=0,len;
        cin>>len>>str;
       // cout<<str<<endl;
        for(int i=0;str[i]!='\0';i++)
        {
            if(str[i]=='0')
                continue;
            if(cnt>=i)
                cnt+= (str[i]-'0');
            else
            {
                ans+= (i-cnt);
                cnt+=(i-cnt+str[i]-'0');
            }
            //cout<<ans<<endl;
        }
        cout<<"Case #"<<x+1<<": "<<ans<<endl;
    }
    return 0;
}
