#include <bits/stdc++.h>
#define MAXA 100005
#define MOD 1000000007
using namespace std;
bool vis[11];
int counta(long int x)
{
    int ans=0;
    while(x!=0)
    {
        int r=x%10;
        if(vis[x%10]==0)
        {
            ans++;
            vis[x%10]=1;
        }
        x=x/10;
    }
    return ans;
}
int main()
{
    freopen("A-large.in","r+",stdin);
    freopen("output1.txt","w+",stdout);
    long int t,n,x=1;
    cin>>t;
    while(t--)
    {
        long int i=1;
        int c=0;
        memset(vis,false,sizeof(vis));
        cin>>n;
        long int temp=n;
        if(n==0)
            printf("Case #%ld: INSOMNIA\n",x);
        else
        {
            while(c!=10)
            {
                temp=n*i;
                c+=counta(temp);
                i++;
            }
            printf("Case #%ld: %ld\n",x,temp);
        }
        x++;
    }
    return 0;
}
