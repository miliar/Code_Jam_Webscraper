#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<queue>
using namespace std;

pair<pair<int,int>,pair<int,int> > z[1010];

int c[1010][1010];
int d[1010];
int v[1010];
queue<int> q;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int TT;
    scanf("%d",&TT);
    for (int T=1;T<=TT;T++)
    {
        int w,h,b;
        scanf("%d%d%d",&w,&h,&b);
        for (int i=0;i<b;i++)
            scanf("%d%d%d%d",&z[i].first.first,&z[i].first.second,&z[i].second.first,&z[i].second.second);
        int s=b+1,t=b+2;
        c[s][t]=w;
        for (int i=0;i<b;i++)
            c[s][i+1]=z[i].first.first;
        for (int i=0;i<b;i++)
            c[i+1][t]=w-1-z[i].second.first;
        for (int i=0;i<b;i++)
            for (int j=0;j<b;j++)
            {
                int tmp=0;
                if (z[i].first.first<z[j].first.first) tmp+=max(0,z[j].first.first-1-z[i].second.first);
                else tmp+=max(0,z[i].first.first-1-z[j].second.first);
                if (z[i].first.second<z[j].first.second) tmp=max(tmp,max(0,z[j].first.second-1-z[i].second.second));
                else tmp=max(tmp,max(0,z[i].first.second-1-z[j].second.second));
                c[i+1][j+1]=tmp;
                //printf("C %d %d: %d %d %d %d %d\n",i+1,j+1,c[i+1][j+1],z[i].first.first,z[i].first.second,z[j].first.first,z[j].first.second);
            }
        memset(v,0,sizeof(v));
        while (!q.empty()) q.pop();
        for (int i=1;i<=b+2;i++)
            d[i]=1000000000;
        d[s]=0;
        v[s]=1;
        q.push(s);
        while (!q.empty())
        {
            int x=q.front();
            for (int i=1;i<=b+2;i++)
            {
                if (d[i]>d[x]+c[x][i])
                {
                    d[i]=d[x]+c[x][i];
                    if (!v[i])
                    {
                        v[i]=1;
                        q.push(i);
                    }
                }
            }
            v[x]=0;
            q.pop();
        }
        printf("Case #%d: %d\n",T,d[t]);
    }
    return 0;
}
