2-sat 模板
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int Maxn=1010,Maxm=1000010;
struct Edge
{
    int from,to,next;
}edge[Maxm*4],edge1[Maxm*4];//edge1是染色之后的边
int box[Maxn*2],top,box1[Maxn*2],top1;
int n;
void add(int from,int to)
{
    edge[top].to=to;
    edge[top].from=from;
    edge[top].next=box[from];
    box[from]=top++;
    edge[top].from=to^1;
    edge[top].to=from^1;
    edge[top].next=box[to^1];
    box[to^1]=top++;
}
struct Time
{
    int x,y,l;
}time[Maxn];
int getTime(int hh,int mm)
{
    return hh*60+mm;
}
bool conflict(int x,int lx,int y,int ly)
{
    if(x>=y&&x<y+ly)return true;
    if(y>=x&&y<x+lx)return true;
    return false;
}
int pred[Maxn*2],deep[Maxn*2],stack[Maxn*2],col[Maxn*2],colnum,tops,cnt;
bool instack[Maxn*2];
bool tarjan(int x)
{
    int min0=deep[x]=pred[x]=cnt++;
    stack[tops++]=x;instack[x]=true;
    for(int i=box[x];i!=-1;i=edge[i].next)
    {
        int x1=edge[i].to;
        if(deep[x1]==-1&&!tarjan(x1))return false;
        if(instack[x1])min0=min(min0,pred[x1]);
    }
    pred[x]=min0;
    if(pred[x]==deep[x])
    {
        bool flag=false;
        while(1)
        {
            int tmp=stack[--tops];
            instack[tmp]=false;
            if(col[tmp]==-1)
            {
                col[tmp]=colnum;
                col[tmp^1]=colnum^1;
                flag=true;
            }
            else if(col[tmp]==(colnum^1))return false;
            if(tmp==x)break;
        }
        if(flag)colnum+=2;
    }
    return true;
}
void add1(int from,int to)
{
    edge1[top1].to=to;
    edge1[top1].next=box1[from];
    box1[from]=top1++;
}
bool ans[Maxn*2];
bool topology()
{
    memset(box1,-1,sizeof(box1));top1=0;
    int que[Maxn*2],in=0,out=0;
    int num[Maxn*2];
    for(int i=0;i<top;++i)
    {
        int x=col[edge[i].from];
        int y=col[edge[i].to];
        if(x==y)continue;
        num[x]++;
        add1(y,x);//加反向边 求拓扑
    }
    for(int i=0;i<colnum;++i)if(num[i]==0)que[in++]=i;
    memset(ans,false,sizeof(ans));
    while(in>out)
    {
        int x1=que[out++];
        for(int i=box1[x1];i!=-1;i=edge1[i].next)
        {
            int x1=edge1[i].to;
            num[x1]--;
            if(num[x1]==0)que[in++]=x1;
        }
        if(ans[x1^1])continue;
        ans[x1]=true;//记录选中的缩点
    }
    return true;
}
bool twoSat()
{
    memset(instack,false,sizeof(instack));
    memset(deep,-1,sizeof(deep));
    memset(col,-1,sizeof(col));
    cnt=colnum=tops=0;
    for(int i=0;i<2*n;++i)
    {
        if(col[i]==-1&&!tarjan(i))return false;
    }
    if(!topology())return false;
    printf("YES\n");
    for(int i=0;i<n;++i)
    {
        if(ans[col[2*i]])
        {
            int tmp=time[i].x;
            printf("%02d:%02d ",tmp/60,tmp%60);
            tmp+=time[i].l;
            printf("%02d:%02d\n",tmp/60,tmp%60);
        }
        else if(ans[col[2*i+1]])
        {
            int tmp=time[i].y-time[i].l;
            printf("%02d:%02d ",tmp/60,tmp%60);
            tmp=time[i].y;
            printf("%02d:%02d\n",tmp/60,tmp%60);
        }
    }
    return true;
}
int main()
{
    freopen("in.txt","r",stdin);
    memset(box,-1,sizeof(box));
    top=0;
    scanf("%d",&n);
    for(int i=0;i<n;++i)
    {
        int hh1,mm1,hh2,mm2;
        scanf("%2d:%2d %2d:%2d%d",&hh1,&mm1,&hh2,&mm2,&time[i].l);
        time[i].x=getTime(hh1,mm1);
        time[i].y=getTime(hh2,mm2);
    }
    for(int i=0;i<n;++i)
    {
        for(int j=i+1;j<n;++j)
        {
            if(conflict(time[i].x,time[i].l,time[j].x,time[j].l))add(2*i,2*j+1);
            if(conflict(time[i].x,time[i].l,time[j].y-time[j].l,time[j].l))add(2*i,2*j);
            if(conflict(time[i].y-time[i].l,time[i].l,time[j].x,time[j].l))add(2*i+1,2*j+1);
            if(conflict(time[i].y-time[i].l,time[i].l,time[j].y-time[j].l,time[j].l))add(2*i+1,2*j);
        }
    }
    if(!twoSat())printf("NO\n");
    return 0;
}
