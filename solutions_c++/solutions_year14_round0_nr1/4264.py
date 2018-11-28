#include<cstdio>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<map>

#define il(n) scanf("%lld",&n)
#define i(n) scanf("%d",&n)

using namespace std;

int main()
{
int i,tc;
cin>>tc;
for(i=1;i<=tc;i++)
{
    int a,arr[5][5],mark[20]={0},j,co=0,ans,k;
    cin>>a;
    for(j=1;j<=4;j++)
    {
        for(k=1;k<=4;k++)
        {
            cin>>arr[j][k];
        }
    }
    for(j=1;j<=4;j++)
    {
        mark[arr[a][j]]++;
    }
    cin>>a;
    for(j=1;j<=4;j++)
    {
        for(k=1;k<=4;k++)
        {
            cin>>arr[j][k];
        }
    }
    for(j=1;j<=4;j++)
    {
        mark[arr[a][j]]++;
    }
    //cout<<"KKK";
    for(j=1;j<=16;j++)
    {
        if(mark[j]==2)
        {
            ans=j;
            co++;
        }
    }
    cout<<"Case #"<<i<<": ";
    if(co==0)
        cout<<"Volunteer cheated!"<<"\n";
    if(co==1)
        cout<<ans<<"\n";
    if(co>1)
        cout<<"Bad magician!"<<"\n";
}
return 0;
}
