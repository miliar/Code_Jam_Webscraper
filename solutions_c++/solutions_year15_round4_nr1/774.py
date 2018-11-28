#include <cstdio>
#include <algorithm>

using namespace std;

char base[105][105];
int getd(char k)
{
    if (k=='v')
        return 0;
    if (k=='>')
        return 1;
    if (k=='^')
        return 2;
    if (k=='<')
        return 3;
    return -1;
}

inline void solvetc(int tcid)
{
    int n,m;
    scanf("%d%d",&n,&m);
    for (int i=1; i<=n; i++)
        scanf("%s",base[i]+1);
    int cnth[105],cntv[105];
    for (int i=1; i<=max(n,m); i++)
    {
        cnth[i]=0;
        cntv[i]=0;
    }
    for (int i=1; i<=n; i++)
        for (int j=1; j<=m; j++)
        {
            cnth[i]+=getd(base[i][j])!=-1;
            cntv[j]+=getd(base[i][j])!=-1;
        }
    for (int i=1; i<=n; i++)
        for (int j=1; j<=m; j++)
            if (getd(base[i][j])!=-1)
                if (cnth[i]==1 && cntv[j]==1)
                {
                    printf("Case #%d: IMPOSSIBLE\n",tcid);
                    return;
                }
    int ret=0;
    int markh[105],markv[105];
    for (int i=1; i<=max(n,m); i++)
        markh[i]=markv[i]=0;
    for (int i=1; i<=n; i++)
        for (int j=1; j<=m; j++)
            if (getd(base[i][j])!=-1)
            {
                if (getd(base[i][j])==3 && markh[i]==0)
                    ret++;
                if (getd(base[i][j])==2 && markv[j]==0)
                    ret++;
                markh[i]++;
                markv[j]++;
            }
    for (int i=1; i<=max(n,m); i++)
        markh[i]=markv[i]=0;
    for (int i=n; i>=1; i--)
        for (int j=m; j>=1; j--)
            if (getd(base[i][j])!=-1)
            {
                if (getd(base[i][j])==1 && markh[i]==0)
                    ret++;
                if (getd(base[i][j])==0 && markv[j]==0)
                    ret++;
                markh[i]++;
                markv[j]++;
            }
    printf("Case #%d: %d\n",tcid,ret);

}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int it;
    scanf("%d",&it);
    for (int i=1; i<=it; i++)
        solvetc(i);
}
