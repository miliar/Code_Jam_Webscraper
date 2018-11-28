#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
int t,n;
int p[1001];
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Infinite House of Pancakes.txt","w",stdout);
    int cas=0,maxp;
    cin>>t;
    while(t--)
    {
        cin>>n;
        memset(p,0,sizeof(p));
        maxp=0;
        for(int i=1;i<=n;i++)
        {
            int num;
            cin>>num;
            maxp=max(maxp,num);
            p[num]++;
        }
        int ans=maxp;
        for(int i=1;i<=maxp;i++)
        {
            int time=i;
            for(int j=i+1;j<=maxp;j++)
                time+=p[j]*(j/i-(j%i==0));
            ans=min(time,ans);
        }
        cout<<"Case #"<<++cas<<": "<<ans<<endl;
    }
}
