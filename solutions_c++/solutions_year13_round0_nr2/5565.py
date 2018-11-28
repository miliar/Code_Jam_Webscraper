#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<string>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<cmath>
#include<list>
#include<cctype>
#include<ctime>
#include<algorithm>
using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define inf -1u>>1
#define MP(x,y) make_pair(x,y)
#define two(x) (1<<x)
#define eps 1e-8
const double pi=acos(-1.0);

/***************By Asakura*****************/
int n,m,mm[15][15];
bool ok(int x,int y)
{
    int i,j;
    int cnt1=0,cnt2=0;
    for(i=0;i<n;i++)
    {
        if(mm[i][y]==1)
            cnt1++;
    }
    for(i=0;i<m;i++)
        if(mm[x][i]==1)
            cnt2++;
    if(cnt1==n||cnt2==m)
        return true;
    return false;
}
int main()
{
    //freopen("B-small-attempt1.in","r",stdin);
    //freopen("B-small-attempt1.out","w",stdout);
    int t,i,j,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                scanf("%d",&mm[i][j]);
        int flag=1;
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
            {
                if(mm[i][j]==1)
                    if(!ok(i,j))
                        flag=0;
            }
        printf("Case #%d: ",++cas);
        if(flag)
            puts("YES");
        else
            puts("NO");
    }
    return 0;
}
