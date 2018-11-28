#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>
using namespace std;

int ok;

struct sweep
{
    int a[5][5];
    bool operator <(const sweep &other) const
    {
        for (int i=0;i<5;i++)
        {
            for (int j=0;j<5;j++)
            {
                if (a[i][j]!=other.a[i][j]) return a[i][j]<other.a[i][j];
            }
        }
    }
};

int n,m,space;
map<sweep, int> mm;
int dx[8]={0,0,1,1,1,-1,-1,-1};
int dy[8]={1,-1,1,0,-1,1,0,-1};

void DFS(sweep tmp)
{
    int i,j,cnt=0;
    if (ok==1) return;
    for (i=0;i<n;i++)
    {
        for (j=0;j<m;j++)
        {
        //    printf("%3d",tmp.a[i][j]);
            if (tmp.a[i][j]==0) cnt++;
        }
      //  printf("\n");
    }
    //printf("....................\n");
    if (cnt==space)
    {
        ok=1;
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                if (i==0 && j==0) printf("c");
                else if (tmp.a[i][j]==0) printf(".");
                else printf("*");
            }
            printf("\n");
        }
        return;
    }
    if (cnt>space) return;
    for (i=0;i<n;i++)
    {
        for (j=0;j<m;j++)
        {
            if (tmp.a[i][j]!=0) continue;
            sweep tmp1;
            for (int ii=0;ii<5;ii++)
            {
                for (int jj=0;jj<5;jj++)
                {
                    tmp1.a[ii][jj]=tmp.a[ii][jj];
                }
            }
            for (int ii=0;ii<8;ii++)
            {
                if (i+dx[ii]<n && i+dx[ii]>=0 && j+dy[ii]<m && j+dy[ii]>=0)
                {
                    tmp1.a[i+dx[ii]][j+dy[ii]]=0;
                }
            }
            // printf("%d...\n",tmp1);
            if (mm[tmp1]!=0) continue;
            mm[tmp1]=1;
            DFS(tmp1);
          //  mm[tmp1]=0;
        }
    }
}


int main()
{
    freopen("C-small-attempt4.in","r",stdin);
    freopen("C.out","w",stdout);
    int i,j,T,x,cnt=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d",&n,&m,&x);
        //printf("%d ..%d ..%d\n",n,m,x);
        sweep tmp;
        space=n*m-x;
        for (i=0;i<5;i++)
        {
            for (j=0;j<5;j++)
            {
                tmp.a[i][j]=1;
            }
        }
        tmp.a[0][0]=0;
        mm.clear();
        mm[tmp]=1;
        ok=0;
        printf("Case #%d:\n",cnt++);
        DFS(tmp);
        if (ok==0) printf("Impossible\n");
    }
    return 0;
}
