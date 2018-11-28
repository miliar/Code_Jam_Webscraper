#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;
#define LL __int64

struct node
{
    int x,id;
}num[101];
int n;
bool cmp(node a,node b)
{
    return a.x < b.x;
}
int p[101];
int judge(LL x)
{
    int i;
    for(i = n-1;i >= 0;i --)
    {
        p[i] = x%10;
        x /= 10;
    }
    for(i = 1;i < n;i ++)
    {
        if(p[i] > p[i-1])
        continue;
        else
        break;
    }
    for(;i < n;i ++)
    {
        if(p[i] < p[i-1])
        ;
        else
        break;
    }
    if(i == n) return 1;
    else return 0;
}
int spfa(LL x)
{
    LL front,s;
    int o[11],i,j;
    if(judge(x)) return 0;
    map<LL,int> mp;
    mp[x] = 0;
    queue<LL>que;
    que.push(x);
    memset(o,0,sizeof(o));
    while(!que.empty())
    {
        front = que.front();
        s = front;
        for(i = n-1;i >= 0;i --)
        {
            o[i] = front%10;
            front /= 10;
        }
        for(i = 0;i < n-1;i ++)
        {
            swap(o[i],o[i+1]);
            LL temp = 0;
            for(j = 0;j < n;j ++)
            temp = temp*10 + o[j];
            if(mp.find(temp) == mp.end())
            {
                mp[temp] = mp[s] + 1;
                if(judge(temp)) return mp[temp];
                que.push(temp);
            }
            swap(o[i],o[i+1]);
        }
        que.pop();
    }
    return 100;
}
int main()
{
    freopen("B-small-attempt5.in","r",stdin);
    freopen("B-small-attempt5.out","w",stdout);
    int i,t,cas = 1;
    LL temp;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(i = 0;i < n;i ++)
        {
            scanf("%d",&num[i].x);
            num[i].id = i;
        }
        sort(num,num+n,cmp);
        for(i = 0;i < n;i ++)
        {
            p[num[i].id] = i;
        }
        temp = 0;
        for(i = 0;i < n;i ++)
        {
            temp = temp*10 + p[i];
        }
        printf("Case #%d: %d\n",cas++,spfa(temp));
    }
    return 0;
}
