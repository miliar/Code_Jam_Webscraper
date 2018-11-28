#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
using namespace std;
typedef long long LL;
const LL Mod = 1000002013LL;
struct Node
{
    int id;
    LL p,num;
};
bool cmp(const Node &a,const Node &b)
{
    if (a.p!=b.p) return a.p<b.p;
    return a.id<b.id;
}
Node a[10010],b[10010];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        LL preCost=0;
        for (int i=0;i<m;i++)
        {
            LL u,v,p;
            scanf("%I64d%I64d%I64d",&u,&v,&p);
            LL pM=p%Mod;
            LL tmp=(v-u)*n%Mod;
            tmp-=((0+v-u-1)*(v-u)/2)%Mod;
            tmp=(tmp%Mod+Mod)%Mod;
            preCost=(preCost+tmp*pM%Mod)%Mod;
            a[i*2].id=0;
            a[i*2].p=u;
            a[i*2].num=p;
            a[i*2+1].id=1;
            a[i*2+1].p=v;
            a[i*2+1].num=p;
        }
        m*=2;
        sort(a,a+m,cmp);
        int cntt=0,now=0;
        LL cost=0;
        for (int i=0;i<m;i++)
        {
            int pos=i;
            long long totP=0;
            while (pos<m&&a[pos].id==a[i].id&&a[pos].p==a[i].p)
            {
                totP+=a[pos].num;
                pos++;
            }
            pos--;
            if (a[i].id==0)
            {
                b[cntt].p=a[i].p;
                b[cntt].num=totP;
                cntt++;
            }
            else
            {
                LL need=totP;
                while (need!=0)
                {
                    totP=min(need,b[cntt-1].num);
                    LL totPM=totP%Mod;
                    LL delta=a[i].p-b[cntt-1].p;
                    LL tot=delta*n%Mod;
                    tot-=(((delta-1)*delta)/2)%Mod;
                    tot=(tot%Mod+Mod)%Mod;
                    cost=(cost+tot*totPM%Mod)%Mod;
                    b[cntt-1].num-=totP;
                    need-=totP;
                    if (b[cntt-1].num==0) cntt--;
                }
            }
            i=pos;
        }
        printf("Case #%d: %I64d\n",ii,((preCost-cost)%Mod+Mod)%Mod);
    }
    return 0;
}
