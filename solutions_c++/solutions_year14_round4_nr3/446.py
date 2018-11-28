#include <iostream>
#include <stdio.h>
#include <string.h>
#define INT_MAX 1e9
using namespace std;
const int MAXN=1000000;
struct hh
{
    int from,to,c,next;
}edges[10000000];
int box[MAXN];
int tu[110][510];
int w,h,b;
int level[MAXN];
int node;
 int q[MAXN+10];
bool makelevel(int s,int t)
{

    //cout<<s<<' '<<t<<endl;
    int i;
    memset(level,0,sizeof(level));
    level[s]=1;

    q[0]=s;
    int head=0,end=1;
    while(head<end)
    {
        for(i=box[q[head]];i!=-1;i=edges[i].next)
        {
            if(!level[edges[i].to]&&edges[i].c)
            {
                level[edges[i].to]=level[q[head]]+1;
                q[end]=edges[i].to;
                end++;
                if(edges[i].to==t)return true;
            }
        }
        head++;
    }
    return false;
}
int dinic(int v,int mincap)
{
    int i;
    if(v==2*node+1)return mincap;
    int ret=0,flow;
    for(i=box[v];i!=-1;i=edges[i].next)
    {
        if(edges[i].c>0&&level[edges[i].to]>level[v])
        {
            int min;
            if(mincap-ret<edges[i].c)min=mincap-ret;
            else min=edges[i].c;
            flow=dinic(edges[i].to,min);
            edges[i].c-=flow;edges[i^1].c+=flow;
            ret+=flow;
            if(ret==mincap)return ret;
        }
    }
    return ret;
}
int aa[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
int nodee[110][502];
void add(int from,int to,int c,int k)
{
    edges[k].from=from;
    edges[k].to=to;
    edges[k].c=c;
    edges[k].next=box[from];
    box[from]=k;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        printf("Case #%d: ",cas);
        memset(tu,0,sizeof(tu));
        memset(box,-1,sizeof(box));
        memset(nodee,-1,sizeof(nodee));
        scanf("%d%d%d",&w,&h,&b);
        for(int i=0;i<b;++i)
        {
            int x0,y0,x1,y1;
            scanf("%d%d%d%d",&x0,&y0,&x1,&y1);
            for(int j=x0;j<=x1;++j)
            {
                for(int k=y0;k<=y1;++k)
                {
                    tu[j][k]=1;
                }
            }
        }
        int top=0;
        node=0;
        for(int i=0;i<w;++i)
        {
            for(int j=0;j<h;++j)
            {
                if(tu[i][j]==0)nodee[i][j]=node++;
            }
        }

        for(int i=0;i<w;++i)
        {
            for(int j=0;j<h;++j)
            {
                if(tu[i][j])continue;
                int id1=nodee[i][j];
                add(id1*2+1,id1*2+2,1,top++);
                add(id1*2+2,id1*2+1,0,top++);

                for(int k=0;k<4;++k)
                {
                    int xx=i+aa[k][0],yy=j+aa[k][1];
                    if(xx<0||xx>=w||yy<0||yy>=h)continue;
                    if(tu[xx][yy])continue;
                    int id2=nodee[xx][yy];
                    //cout<<id1<<' '<<id2<<endl;
                    add(id1*2+2,id2*2+1,1,top++);
                    add(id2*2+1,id1*2+2,0,top++);
                }
            }
        }
        for(int i=0;i<w;++i)
        {
            if(tu[i][0])continue;
            int id=nodee[i][0];
            add(0,2*id+1,1,top++);
            add(2*id+1,0,0,top++);
        }
        for(int i=0;i<w;++i)
        {
            if(tu[i][h-1])continue;
            int id=nodee[i][h-1];
            add(2*id+2,node*2+1,1,top++);
            add(node*2+1,2*id+2,0,top++);
        }
        int ans=0;
       // cout<<node*2+1<<endl;
        while(makelevel(0,node*2+1))
        {
          //  cout<<"dd"<<endl;
            ans+=dinic(0,INT_MAX);
            }
        printf("%d\n",ans);
    }
}
