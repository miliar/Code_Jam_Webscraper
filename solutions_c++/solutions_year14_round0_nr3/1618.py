#include<cstdio>
#include<queue>
#include<algorithm>
using namespace std;
struct state
{
   char d[55][55];
   int n,x,y;
   bool operator <(const state a)const
   {
        return n>a.n;
   };
}sw;
priority_queue<state> pq;
queue<pair<int,int> > q;
char x[55][55];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,r,m,c,n;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        scanf("%d%d%d",&r,&c,&m);
        n=r*c-m;
        for(int i=0,R=r+1;i<=R;i++)
            for(int j=0,C=c+1;j<=C;j++)
                if(i>0&&i<R&&j>0&&j<C)
                    sw.d[i][j]='*';
                else
                    sw.d[i][j]='#';
        sw.d[1][1]='.';
        sw.n=1;
        sw.x=1;
        sw.y=1;
        pq.push(sw);
        while(!pq.empty())
        {
            sw=pq.top();
            if(sw.n==n)
                break;
            else if(sw.n<n)
            {
                for(int i=sw.x-1;i<=sw.x+1;i++)
                    for(int j=sw.y-1;j<=sw.y+1;j++)
                        if(sw.d[i][j]=='*')
                        {
                            q.push(make_pair(i,j));
                            sw.d[i][j]='.';
                            sw.n++;
                        }
                while(!q.empty())
                {
                    sw.x=q.front().first;
                    sw.y=q.front().second;
                    pq.push(sw);
                    q.pop();
                }
            }
            pq.pop();
        }


        if(pq.empty())
            printf("Case #%d:\nImpossible\n",I);
        else
        {
            sw=pq.top();
            sw.d[1][1]='c';
            printf("Case #%d:\n",I);
            for(int i=1;i<=r;i++)
            {
                for(int j=1;j<=c;j++)
                    printf("%c",sw.d[i][j]);
                printf("\n");
            }
        }

        while(!pq.empty())
            pq.pop();
    }
}
