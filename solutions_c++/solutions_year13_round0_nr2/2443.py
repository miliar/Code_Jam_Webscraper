#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#include<ctime>
#include<set>
#include<string>
using namespace std;
const int MAX=200005;
const int inf=1<<30;
#define ll long long
#define PB push_back
#define PII pair<int,int>
#define MP(x,y) make_pair(x,y)
int mp[105][105],n,m;
int r[105],c[105];
int main()
{
    int i,j,k,T;
    freopen("B-large.in","r",stdin);
    freopen("2.txt","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)
        {
            r[i]=0;
            for(j=1;j<=m;j++)
            {
                scanf("%d",&mp[i][j]);
                r[i]=max(r[i],mp[i][j]);
            }
        }
        for(i=1;i<=m;i++)
        {
            c[i]=0;
            for(j=1;j<=n;j++)
                c[i]=max(c[i],mp[j][i]);
        }
        bool flag=true;
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
                if(r[i]!=mp[i][j]&&c[j]!=mp[i][j])
                    flag=false;
        printf("Case #%d: ",cas);
        if(flag)
            puts("YES");
        else
            puts("NO");
    }
    return 0;
}
