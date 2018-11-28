#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;

int res;
int p[1<<20];
int n,m,k;
int t;
int s[20][20];
int work(int id)
{
    int tmp=0;
    memset(s,0,sizeof(s));
    for(int i=0;i<t;i++)
    {
        if(id&(1<<i))
        {
            s[i/m][i%m]=1;
        }
    }
    for(int i=0;i<n-1;i++)
    for(int j=0;j<m-1;j++)
    {
        if(s[i][j])
        {
            if(s[i][j+1]) tmp++;
            if(s[i+1][j]) tmp++;
        }
    }
    for(int j=0;j<m-1;j++)
    {
        if(s[n-1][j])
        {
            if(s[n-1][j+1]) tmp++;
        }
    }
    for(int i=0;i<n-1;i++)
    {
        if(s[i][m-1])
        {
            if(s[i+1][m-1]) tmp++;
        }
    }
    return tmp;
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    p[0]=0;
    for(int i=1;i<(1<<18);i++)
    p[i]=p[i>>1] +i%2;
    int T;
    scanf("%d",&T);
    int cas=0;
    while(T--)
    {
        scanf("%d%d%d",&n,&m,&k);
        t=n*m;
        res=4*n*m;
        for(int i=0;i<(1<<t);i++)
        {
            if(p[i]==k)
            {
                res=min(res,work(i));
            }
        }
        printf("Case #%d: %d\n",++cas,res);
    }
    return 0;
}
