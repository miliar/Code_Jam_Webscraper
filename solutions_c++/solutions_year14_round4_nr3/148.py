#include<cstdio>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cstdlib>
using namespace std;
struct rect
{
    int x1,y1,x2,y2;
};
int zz,z,w,h,n,d,x;
priority_queue<pair<int,int> > pq;
bool v[2000];
rect a[2000];
int dist(rect a,rect b)
{
    if(a.x1<=b.x2 && b.x1<=a.x2)
        return min(abs(b.y1-a.y2)-1,abs(b.y2-a.y1)-1);
    else if(a.y1<=b.y2 && b.y1<=a.y2)
        return min(abs(b.x1-a.x2)-1,abs(b.x2-a.x1)-1);
    else
        return max(min(abs(b.y1-a.y2)-1,abs(b.y2-a.y1)-1),
                   min(abs(b.x1-a.x2)-1,abs(b.x2-a.x1)-1));
    return 0;
}
int main()
{
    freopen("c-large.out","w",stdout);
    freopen("c-large.in","r",stdin);
    scanf("%d",&z);
    for(int zz=1;zz<=z;zz++)
    {
        scanf("%d %d %d",&w,&h,&n);
        a[0]=(rect){-1,0,-1,h-1};
        a[1]=(rect){w,0,w,h-1};
        for(int i=2;i<n+2;i++)
        {
            scanf("%d%d%d%d",&a[i].x1,&a[i].y1,&a[i].x2,&a[i].y2);
        }
        n+=2;
        while(!pq.empty())
            pq.pop();
        pq.push(make_pair(0,0));
        memset(v,0,sizeof(v));
        while(!pq.empty())
        {
            d=-pq.top().first;
            x=pq.top().second;
            pq.pop();
            if(v[x])
                continue;
            if(x==1)
            {
                printf("Case #%d: %d\n",zz,d);
                break;
            }
            v[x]=true;
            for(int i=0;i<n;i++)
                if(!v[i])
                    pq.push(make_pair(-(d+dist(a[i],a[x])),i));
        }
    }
    return 0;
}
