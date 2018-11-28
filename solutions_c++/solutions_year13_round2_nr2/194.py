#include<iostream>
#include<sstream>
#include<cstdio>
#include<cctype>
#include<string>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<vector>
#include<cstring>
#include<algorithm>

#define ll long long
#define inf 1000000009
#define mod 1000000007

using namespace std;

typedef pair<int,int> II;
/*double C(int n,int m)
{
    double ret=1.;
    for(int i=1;i<=m;i++) ret*=n-i+1;
    for(int i=1;i<=m;i++) ret/=i;
    return ret;
}
*/
double f[5000][5000];
double go()
{
    int n,x,y,p=1;
    cin>>n>>x>>y;
    if(x<0) x*=-1;
    while(1)
    {
        if(n<4*p-3) break;
        n-=4*p-3;
        p++;
    }
    if(x+y<=2*p-4) return 1;
    if(x+y>2*p-2) return 0;
    int tot=4*p-3;
    int cnt=y+1;
    if(cnt>n) return 0;    
    memset(f,0,sizeof(f));
    f[0][0]=1.;
    for(int i=0;i<n;i++)
        for(int j=max(0,i-tot/2);j<=i&&j<=tot/2;j++)
        {
            if(j==tot/2)
            {
                f[i+1][j]+=f[i][j];
            }
            else if(i-j==tot/2)
            {
                f[i+1][j+1]+=f[i][j];
            }
            else
            {
                f[i+1][j]+=0.5*f[i][j];
                f[i+1][j+1]+=0.5*f[i][j];
            }
        }
    double res=0.;
    for(int i=cnt;i<=n;i++) res+=f[n][i];
    return res;
}

int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;
    cin>>T;
    for(int run=1;run<=T;run++)
    {
        printf("Case #%d: %.12lf\n",run,go());
    }
    fclose(stdout);
}
