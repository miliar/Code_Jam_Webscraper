#include<cstdio>
#include<map>
#include<conio.h>
using namespace std;
struct yo
{
    int n;
    int x[31];
    int y[31];
    bool operator< (const yo &r) const
    {
        for (int i=0;i<n;i++)
        {
            if (x[i]!=r.x[i])
                return x[i]<r.x[i];
            if (y[i]!=r.y[i])
                return y[i]<r.y[i];
        }
        return false;
    }
    yo* operator= (const yo &r)
    {
        n = r.n;
        for (int i=0;i<n;i++)
        {
            x[i] = r.x[i];
            y[i] = r.y[i];
        }
        return this;
    }
    bool empty (int xx,int yy)
    {
        for (int i=0;i<n;i++)
            if (x[i]==xx and y[i]==yy)
                return false;
        return true;
    }
    void add (int xx,int yy)
    {
        x[n] = xx;
        y[n] = yy;
        n++;
    }
};
map<yo,double> M[2];
map<pair<int,int>,double> ans,solve[21];
yo board;
void dfs (int x,int y,double prop,int next)
{
    if (prop<.0000001)
        return;
    //printf("%d %d\n",x,y);
    if (y==0)
    {
        yo temp=board;
        temp.add(x,y);
        M[next][temp] += prop;
        return;
    }
    if (board.empty(x,y-2) and y>=2)
    {
        dfs (x,y-2,prop,next);
        return;
    }
    if (board.empty(x-1,y-1) and board.empty(x+1,y-1))
    {
        if (y==1)
        {
            dfs (x,y-1,prop,next);
            return;
        }
        dfs (x-1,y-1,prop/2.0,next);
        dfs (x+1,y+1,prop/2.0,next);
        return;
    }
    if (board.empty(x-1,y-1))
        dfs (x-1,y-1,prop,next);
    else if (board.empty(x+1,y-1))
        dfs (x+1,y+1,prop,next);
    else
    {
        yo temp=board;
        temp.add(x,y);
        M[next][temp] += prop;
    }
}
void drop (double prop,int next)
{
    dfs (0,26,prop,next);
}
void plusans (double prop)
{
    int i,x,y;
    for (i=0;i<board.n;i++)
    {
        x = board.x[i];
        y = board.y[i];
        ans[make_pair(x,y)] += prop;
    }
}
int main()
{
    yo temp;
    int i,now,next;
    //freopen("genB.txt","w",stdout);
    map<yo,double>::iterator it;
    map<pair<int,int>,double>::iterator it2;
    temp.n = 0;
    M[1][temp] = 1;
    for (i=1;i<=20;i++)
    {
        now = i%2;
        next = (i+1)%2;
        /*
        for (it2=ans.begin();it2!=ans.end();it2++)
            printf("%d %d : %lf\n",it2->first.first,it2->first.second,it2->second);
        printf("\n");
        for (it=M[now].begin();it!=M[now].end();it++)
        {
            board = it->first;
            printf("\t%lf\n",it->second);
            for (int j=0;j<board.n;j++)
                printf("\t\t(%d,%d)\n",board.x[j],board.y[j]);
            printf("\n");
        }
        printf("\n\n");*/
        for (it=M[now].begin();it!=M[now].end();it++)
        {
            board = it->first;
            drop(it->second,next);
        }
        for (it=M[next].begin();it!=M[next].end();it++)
        {
            board = it->first;
            plusans(it->second);
        }
        for (it2=ans.begin();it2!=ans.end();it2++)
            solve[i][it2->first] = it2->second;
        ans.clear();
        M[now].clear();
    }
    int T,t,n,x,y;
    freopen("B-small-attempt0 (1).in","r",stdin);
    freopen("B-small-attempt0 (1).out.txt","w",stdout);
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        scanf("%d %d %d",&n,&x,&y);
        printf("Case #%d: ",t);
        it2 = solve[n].find(make_pair(x,y));
        if (it2==solve[n].end())
            printf("0");
        else
            printf("%lf",it2->second);
        printf("\n");
    }
    return 0;
}
