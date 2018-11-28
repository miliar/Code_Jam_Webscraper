#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
int t,n;
char s[1010];
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Standing Ovation.txt","w",stdout);
    int cas=0;
    cin>>t;
    while(t--)
    {
        cin>>n;
        cin>>s;
        int ans=0,cur=0;
        for(int i=0;i<=n;i++)
        {
            int num=s[i]-'0';
            if(i>cur)
                ans+=(i-cur),cur+=(i-cur);
            cur+=num;
        }
        cout<<"Case #"<<++cas<<": "<<ans<<endl;

    }
}
