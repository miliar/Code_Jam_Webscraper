#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include<iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;
int ans,n;
struct Node
{
    int v,id;
}node[1100];
int pos[1100];
bool cmp1(Node a,Node b)
{
    return a.v<b.v;
}
bool cmp0(Node a,Node b)
{
    return a.id<b.id;
}
int t;
int Find(int p)
{
    int tmp=0;
    for(int i=1;i<p;i++)
    if(node[i].v>node[p].v) tmp++;
    return tmp;
}
int main()
{
   freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    int cas=0;
    scanf("%d",&T);
    while(T--)
    {
        ans=0;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&node[i].v);
            node[i].id=i;
        }
        sort(node+1,node+1+n,cmp1);
        for(int i=1;i<=n;i++)
        pos[i]=node[i].id;
        sort(node+1,node+1+n,cmp0);
        for(int i=1;i<n;i++)
        {
            int x=Find(pos[i]);
            ans+=min(x,n-i-x);
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
