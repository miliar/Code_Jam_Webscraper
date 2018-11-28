#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[11111],n,c;
bool v[11111];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int ca=1;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&c);
        for(int i=0;i<n;i++)scanf("%d",&a[i]);
        sort(a,a+n);
        memset(v,0,sizeof(v));
        int ans=0;
        for(int i=n-1;i>=0;i--)
        {
            if(!v[i])
            {
                v[i]=1;
                ans++;
                for(int j=i-1;j>=0;j--)
                {
                    if(a[i]+a[j]<=c&&v[j]==0)
                    {
                        v[j]=1;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",ca++,ans);
    }
    return 0;
}
