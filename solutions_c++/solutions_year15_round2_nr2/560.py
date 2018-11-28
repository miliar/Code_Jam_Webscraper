#include<cstdio>
#include<algorithm>
using namespace std;


int use[110][110];

int getans(int mask, int r, int c)
{
    int nowmask = 1;
    for(int i=0;i<r;i++)
    for(int j=0;j<c;j++)
    {
        if(mask & nowmask)
            use[i][j] = 1;
        else
            use[i][j] = 0;
        nowmask <<= 1;
    }

    int ret = 0;
    for(int i=0;i<r;i++)
    for(int j=0;j<c;j++)
    {
        if(j<c-1)ret += use[i][j]&&use[i][j+1];
        if(i<r-1)ret += use[i][j]&&use[i+1][j];
    }

    return ret;
}

int solve(int r,int c,int n)
{
    int ret = 0x3f3f3f3f;
    int nn = r*c;
    for(int i=0;i<(1<<nn);i++)
    {
        int cc = __builtin_popcount(i);
        if(cc != n)
            continue;
        ret = min(ret, getans(i,r,c));
    }
    return ret;
}

int main()
{
    int ti;scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        int r,c,n;scanf("%d%d%d",&r,&c,&n);
        printf("Case #%d: %d\n",ca,solve(r,c,n));
    }
}
