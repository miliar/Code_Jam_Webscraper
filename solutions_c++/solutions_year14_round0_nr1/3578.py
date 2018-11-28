#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<vector>
#include<map>
#include<algorithm>
#include<limits.h>
#include<set>
#include<math.h>
 
using namespace std;
#define lli long long int
#define ulli unsigned long long int
#define in(t) scanf("%d",&t)
#define inl(t) scanf("%ld",&t)
#define inll(t) scanf("%lld",&t)
#define inlu(t) scanf("%llu",&t)
#define MOD 1000000007

int main()
{
    
    #ifndef ONLINE_JUDGE
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    #endif
    
    int t,a[5][5],b[5][5],i,j,c1,ans,c,x,y;
    in(t);
    for(c=1;c<=t;c++)
    {
    int count[17]={0};
    c1=ans=0;
    in(x);
    x--;
    for(i=0;i<4;i++)
    {
    for(j=0;j<4;j++)
    in(a[i][j]);
    }
    
    in(y);
    y--;
    for(i=0;i<4;i++)
    {
    for(j=0;j<4;j++)
    in(b[i][j]);
    }
    
    for(j=0;j<4;j++)
    count[a[x][j]]++;
    
    for(j=0;j<4;j++)
    count[b[y][j]]++;
    
    for(i=0;i<4;i++)
    {
    if(count[a[x][i]]==2)
    {
    c1++;
    ans=a[x][i];
    }
    }
    
    if(c1==1)
    cout<<"Case #"<<c<<": "<<ans<<"\n";
    
    else if(c1>1)
    cout<<"Case #"<<c<<": "<<"Bad magician!\n";
    
    else if(c1==0)
    cout<<"Case #"<<c<<": "<<"Volunteer cheated!\n";
    }
    return 0;
}
