#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<string.h>
#include<queue>
#define M 1000000007
using namespace std;
main()
{
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k,n,m,standing=0,ans=0,t,q;
    string s;
    cin>>t;
    for(q=1;q<=t;q++)
    {
        standing=0;
        ans=0;


    cin>>n>>s;
    for(i=0;i<=n;i++)
    {
        if(standing>=(i))
        {
            standing+=(s[i]-'0');
        }
        else
        {
            ans+=(i-standing);

            standing=i+(s[i]-'0');
        }

    }
   cout<<"Case #"<<q<<": "<<ans<<endl;
    }
    return 0;
}
