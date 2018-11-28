#include<bits/stdc++.h>
#define ll long long int
#define inf 1000000000
#define mod 1073741824
using namespace std;

ll t,tt,ans,len,i;
char ch,str[101];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    tt=t;
    while(t)
    {
        cin>>str;
        ans=0;
        len=strlen(str);
        if(len==1)
        {
            if(str[0]=='-')
                cout<<"Case #"<<tt-t+1<<": 1"<<endl;
            else
                cout<<"Case #"<<tt-t+1<<": 0"<<endl;

            t--;
            continue;

        }
        ch=str[0];
        for(i=1;i<len;i++)
        {
            if(str[i]!=str[i-1])
            {
                ans+=1;
                ch=str[i];
            }

        }
        if(ch=='-')
            ans++;

        cout<<"Case #"<<tt-t+1<<": "<<ans<<endl;
        t--;
    }

    return 0;
}

