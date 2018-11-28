#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <ctime>

#define ll long long


using namespace std;

int n,m,testnum,ans;
char a[1111][1111];

bool check(int tx, int ty, int dx, int dy)
{
    tx+=dx; ty+=dy;
    while (tx>=0 && ty>=0 && tx<n && ty<m)
    {
        if (a[tx][ty]!='.') return true;
        tx+=dx; ty+=dy;
    }
    return false;
}

int main(int argc, char* argv[])
{
    freopen("/Users/Dora/Desktop/ex/ex/x.in","r",stdin);
    freopen("/Users/Dora/Desktop/ex/ex/x.out","w",stdout);
    scanf("%d",&testnum);
    for (int test=1; test<=testnum; ++test)
    {
        scanf("%d %d",&n,&m);
        for (int i=0; i<n; ++i)
            scanf("%s",a[i]);
        ans=0;
        for (int i=0; i<n; ++i)
        {
            if (ans==-1) break;
            for (int j=0; j<m; ++j)
            {
            if (ans==-1) break;
            if (a[i][j]!='.')
            {
                int dx,dy;
                if (a[i][j]=='>') {dx=0; dy=1;}
                if (a[i][j]=='<') {dx=0; dy=-1;}
                if (a[i][j]=='^') {dx=-1; dy=0;}
                if (a[i][j]=='v') {dx=1; dy=0;}
                if (check(i,j,dx,dy)) continue;
                ans+=1;
                {dx=0; dy=1;if (check(i,j,dx,dy)) continue;}
                {dx=0; dy=-1;if (check(i,j,dx,dy)) continue;}
                {dx=-1; dy=0;if (check(i,j,dx,dy)) continue;}
                {dx=1; dy=0;if (check(i,j,dx,dy)) continue;}
                ans=-1;
            }
            }
        }
        //scanf("%d",&n);
        //for (int i=0; i<n; ++i) scanf("%d",a+i);
        if (ans!=-1)
        printf("Case #%d: %d\n",test,ans);
        else printf("Case #%d: %s\n",test,"IMPOSSIBLE");
    }
}