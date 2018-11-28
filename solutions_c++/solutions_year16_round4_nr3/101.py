#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>

using namespace std;

int nxt[1005];
int pre[1005];

int mtc[1005];
int done[1005];

int base[105][105];
int dir[4][2]=
{
    {
        -1,0,
    },
    {
        0,-1,
    },
    {
        1,0,
    },
    {
        0,1,
    }
};

int r,c;

pair < pair <int,int> , int > place(int id)
{
    if (id<=c)
        return make_pair( make_pair(0,id),2);
    if (id<=r+c)
        return make_pair( make_pair(id-c,c+1),1);
    if (id<=r+c*2)
        return make_pair( make_pair (r+1,(c+1)-(id-r-c)),0);
    if (id<=r*2+c*2)
        return make_pair ( make_pair((r+1)-(id-(2*c+r)),0),3);

}

void solvetp()
{
    scanf("%d%d",&r,&c);
    memset(base,0,sizeof(base));
    memset(done,0,sizeof(done));
    for (int i=1; i<=(r+c); i++)
    {
        int x,y;
        scanf("%d%d",&x,&y);
        mtc[x]=y;
        mtc[y]=x;
    }
    for (int i=1; i<=2*(r+c); i++)
    {
        int t=(i)%(2*(r+c))+1;
        nxt[i]=t;
        pre[t]=i;
    }
    int n=2*(r+c);
    queue <int> par;
    for (int i=1; i<=n; i++)
    {
        if (nxt[i]==mtc[i] && done[i]==0)
        {
            par.push(i);
            done[i]=1;
            done[mtc[i]]=1;
        }
    }
    int cnt=0;
    int ok=1;
    while (ok && par.size())
    {
        int u=par.front();
        //printf("RUN %d\n",u);
        cnt++;
        par.pop();
        auto start=place(u);
        int x,y;
        x=pre[u];
        y=nxt[nxt[u]];
        nxt[x]=y;
        pre[y]=x;
        if (nxt[x]==mtc[x] && done[x]==0)
        {
            done[x]=1;
            done[mtc[x]]=1;
            par.push(x);
        }
        int step=0;
        int done=0;
        x=start.first.first;
        y=start.first.second;
        int dr=start.second;
        while (step<150 && done==0)
        {
            //printf("%d %d %d\n",x,y,dr);
            step++;
            x+=dir[dr][0];
            y+=dir[dr][1];
            start=place(mtc[u]);
            if (x==start.first.first && y==start.first.second)
            {
                done=1;
                continue;
            }
            if (x>0 && x<=r && y>0 && y<=c)
            {
                if (base[x][y]==0)
                {
                    if (dr==0 || dr==2)
                        base[x][y]=1;
                    else
                        base[x][y]=3;
                    //printf("PLACE %d %d %d\n",x,y,base[x][y]);
                }
                //printf("base %d ",base[x][y]);

                dr=dr^base[x][y];
            }
        }
        if (done==0)
        {
            ok=0;
            break;
        }
        //printf("%d %d %d\n",start.first.first,start.first.second,start.second);

    }
    if (ok && cnt==r+c)
    {
        for (int i=1; i<=r; i++)
        {
            for (int j=1; j<=c; j++)
            {
                printf("%c",base[i][j]==1?'\\':'/');
            }
            printf("\n");
        }
    }
    else
        printf("IMPOSSIBLE\n");
}

int main()
{
    freopen("D:/in.txt","r",stdin);
    freopen("D:/out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int itr=1; itr<=tc; itr++)
    {
        printf("Case #%d:\n",itr);
        solvetp();
    }

}
