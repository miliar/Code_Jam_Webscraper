#include<cstdio>
#include<cstring>
#include<queue>
using namespace std;
const int maxn=1e3;
const int d=10;
int T,n,cas=1;
int a[maxn+d];
priority_queue<int> pq;
bool jud(int m)
{
    while (!pq.empty()) pq.pop();
    for (int i=0;i<n;i++) pq.push(a[i]);
    int t=0;
    while (!pq.empty())
    {
        int u=pq.top();pq.pop();
        if (u+t<=m) return 1;
        if (u<=1)
        {
            t+=u;
            break;
        }
        t++;
        int x=u>>1,y=u-x;
        pq.push(x);
        pq.push(y);
    }
    return t<=m;
}
int solve()
{
    int l=0,r=1010,m,ans;
    while (l<=r)
    {
        m=(l+r)>>1;
        if (jud(m)) r=m-1,ans=m;
        else l=m+1;
    }
    return ans;
}
int solve2()
{
    int ret=-1;
    for (int i=0;i<n;i++) if (ret==-1||ret<a[i]) ret=a[i];
    for (int i=1;i<=maxn;i++)
    {
        int sum=0;
        for (int j=0;j<n;j++) sum+=(a[j]+i-1)/i-1;
        if (ret==-1||ret>sum+i) ret=sum+i;
    }
    return ret;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d",&n);
        for (int i=0;i<n;i++) scanf("%d",&a[i]);
        //printf("%d\n",n);
        //for (int i=0;i<n;i++) printf("%d%c",a[i]," \n"[i==n-1]);
        printf("Case #%d: %d\n",cas++,solve2());
    }
    return 0;
}
