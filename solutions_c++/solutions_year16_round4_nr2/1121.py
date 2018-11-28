#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
#include<vector>
#include<cmath>
#include<map>
#include<set>
using namespace std;
typedef long long ll;
const int N=200+1;
double a[N],b[N][N];
int n,k;
double ans=0;
void dfs(int x,int y)
{
    if(y==k+1){ans=max(ans,b[k][k/2]);return;}
    int i,j;
    for(i=x;i<n-k+y;i++)
    {
        b[y][0]=b[y-1][0]*(1-a[i]);
        for(j=1;j<=y;j++)b[y][j]=b[y-1][j]*(1-a[i])+b[y-1][j-1]*a[i];
        dfs(i+1,y+1);
    }
}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int t,tt;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        int i,j,l;ans=0;
        cin>>n>>k;memset(b,0,sizeof b);
        for(i=0;i<n;i++)scanf("%lf",a+i);
        b[0][0]=1.0;
        dfs(0,1);
        printf("Case #%d: %.10f\n",tt,ans);
    }
    return 0;
}
