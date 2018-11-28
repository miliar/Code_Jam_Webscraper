#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <sstream>
using namespace std;
const int inf=1000000000;
int S,T,tot,b[8010],a[10000000][3];
char buf[10000000];
map <string,int> M;
int hash(const string &s)
{
    if (!M.count(s))
    {
        int id=M.size()+1;
        M[s]=id;
    }
    return(M[s]);
}
void add(int x,int y,int z)
{
    a[++tot][0]=y,a[tot][1]=z,a[tot][2]=b[x],b[x]=tot;
    a[++tot][0]=x,a[tot][1]=0,a[tot][2]=b[y],b[y]=tot;
}
int d[8010],q[8010];
bool build()
{
    int l,r;
    q[l=r=1]=S;
    memset(d,0,sizeof(d));
    d[S]=1;
    while (l<=r)
    {
        int x=q[l++];
        for (int i=b[x];i;i=a[i][2])
        {
            int y=a[i][0];
            if (!a[i][1] || d[y])
                continue;
            d[y]=d[x]+1;
            q[++r]=y;
            if (y==T)
                return(true);
        }
    }
    return(false);
}
int dinic(int x,int flow)
{
    if (x==T)
        return(flow);
    int k=flow;
    for (int i=b[x];i;i=a[i][2])
    {
        int y=a[i][0];
        if (d[y]!=d[x]+1 || !a[i][1])
            continue;
        int t=dinic(y,min(k,a[i][1]));
        k-=t;
        a[i][1]-=t;
        a[i^1][1]+=t;
        if (k==0)
            break;
    }
    if (k==flow)
        d[x]=-1;
    return(flow-k);
}
int main()
{
    int TT;
    scanf("%d",&TT);
    while (TT--)
    {
        int n;
        scanf("%d",&n);
        int limit=2000+n*10;
        S=2*limit+1;
        T=S+1;
        tot=1;
        memset(b,0,sizeof(b));
        M.clear();
        gets(buf);
        for (int i=1;i<=n;i++)
        {
            gets(buf);
            stringstream sin(buf);
            vector <int> word;
            string tmp;
            while (sin>>tmp)
                word.push_back(hash(tmp));
            for (int j=0;j<word.size();j++)
            {
                int x=word[j];
                if (i==1)
                    add(S,x,inf);
                else if (i==2)
                    add(x+limit,T,inf);
                else
                    for (int k=0;k<word.size();k++)
                    {
                        int y=word[k];
                        if (x!=y)
                            add(x+limit,y,inf);
                    }
            }
        }
        for (int i=1;i<=limit;i++)
            add(i,i+limit,1);
        int ans=0;
        while (build())
            ans+=dinic(S,inf);
        static int id=0;
        printf("Case #%d: %d\n",++id,ans);
    }
    return(0);
}

