#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int test,n,ans,p;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        string str;
        ans=0,p=0;
        scanf("%d",&n);
        cin>>str;
        for(int i=0;i<=n;i++)
        {
            //cout<<str[i]<<endl;
            if(str[i]=='0')
              continue;
           // cout<<i<<" "<<p<<endl;
            if(i>p)
            {
                ans+=(i-p);
                p+=(i-p);
            }
            p+=str[i]-'0';
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
