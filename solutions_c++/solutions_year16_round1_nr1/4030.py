#include<bits/stdc++.h>
#include<string>
using namespace std;
#define ll int
#define sc1int(x) scanf("%d",&x)
#define sc2int(x,y) scanf("%d%d",&x,&y)
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
     int test,maxx,i,j;
    cin>>test;
    for(int k=1;k<=test;k++)
    {
        maxx=-1;
        string str,ans;
        cin>>str;
        int len=str.length();
        for(int i=0;i<len;i++)
        {
            j=str[i]-'A';
            if(j==maxx)
                ans=str[i]+ans;
            else if(j>maxx)
            {
                maxx=j;
                ans=str[i]+ans;
            }
            else
                ans=ans+str[i];
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
}
