/*
#include<stdio.h>
#include<string.h>
#define N 200005
int n,m;
int s[N],cnt[N];
int f[N];
int lowbit(int x)
{
    return x&(-x);
}
int find(int x)
{
   if(x==f[x]) return x;
   return find(f[x]);
}
void insert(int x,int y)
{
    while(x<=n)
    {
        s[x]+=y;
        x+=lowbit(x);
    }
}
int get_sum(int x)
{
    int sum=0;
    while(x>0)
    {
        sum+=s[x];
        x-=lowbit(x);
    }
    return sum;
}
int main()
{
    int i;
    while(~scanf("%d%d",&n,&m))
    {
        for(i=0;i<=n;i++)
            {cnt[i]=1;f[i]=i;}
            insert(1,n);
            int g=n;
        for(i=0;i<m;i++)
        {
            int mark;
            scanf("%d",&mark);
            if(mark==0)
               {
                   int a,b;
                   scanf("%d%d",&a,&b);
                   int fa=find(a);
                   int fb=find(b);
                   if(fa!=fb)
                    {
                        insert(cnt[fa],-1);
                        insert(cnt[fb],-1);
                        insert(cnt[fb]=cnt[fb]+cnt[fa],1);
                        f[fa]=fb;
                        g--;
                    }
               }
               else
               {
                   int k;
                   scanf("%d",&k);
                   k=g-k+1;
                   int l=1,r=n;
                   while(l<=r)
                   {
                       int mid=(l+r)/2;
                       if(get_sum(mid)>=k)
                        r=mid-1;
                       else
                        l=mid+1;
                   }
                   printf("%d\n",l);
               }
        }

    }
}
/*#include <stdio.h>

#define MAXN 300000

int a[MAXN], c[MAXN], f[MAXN];
int n, m;

int lowbit(int x)
{
    return x & -x;
}

int find(int x)
{
    if (x != f[x])
        f[x] = find(f[x]);
    return f[x];
}

void add(int x, int num)
{
    for ( ; x <= n; x += lowbit(x))
        c[x] += num;
}

int sum(int x)
{
    int sum = 0;
    for ( ; x > 0; x -= lowbit(x))
        sum += c[x];
    return sum;
}




int main()
{
    int i, num, cmd, x, y, k, l, r;

    scanf("%d%d", &n, &m);
    for (i = 1; i <= n; i++)
        f[i] = i;
    for (i = 1; i <= n; i++)
        a[i] = 1;
    add(1, n);//a[i]表示组内有i只猫的组数
    num = n;
    for (i = 1; i <= m; i++)
    {
        scanf("%d", &cmd);
        if (cmd == 0)
        {
            scanf("%d%d", &x, &y);
            x = find(x);
            y = find(y);
            if (x == y)
                continue;
            add(a[x], -1);
            add(a[y], -1);
            add(a[y] = a[x] + a[y], 1);
            f[x] = y;
            num--;//合并集合
        }
        else
        {
            scanf("%d", &k);
            k = num - k + 1;
            l = 1;
            r = n;//二分逼近求第k大值，就是求第num - k + 1小的值
            while (l <= r)
            {
                int mid = (l + r) / 2;
                if (sum(mid) >= k)//注意这里是>=,因为是求第num - k + 1小的，所以尽量往左逼近
                    r = mid - 1;
                else
                    l = mid + 1;
            }
            printf("%d\n", l);
        }
    }
    return 0;
}
#include<stdio.h>
#define N 1005
struct node{int f;int x;int y;}s[N];
int n,t;
bool v[N];
void init()
{
    for(int i=0;i<N;i++)
        {s[i].f=i;v[i]=false;}
}
int find(int x)
{
    if(x==s[x].f) return x;
    return find(s[x].f);
}
int merge(int x,int y)
{
    int fx=s[x].f;
    int fy=s[y].f;
    if(fx!=fy)
        if((s[fx].x-s[fy].x)*(s[fx].x-s[fy].x)+(s[fx].y-s[fy].y)*(s[fx].y-s[fy].y)<=t*t)
            s[fx].f=fy;
}
int main()
{
    int n,t,i,a,b;
    char c[2];
    while(~scanf("%d%d",&n,&t))
    {
        init();
        for(i=1;i<=n;i++)
        {
            scanf("%d%d",&s[i].x,&s[i].y);
            //merge(s[i].x,s[i].y);
        }
        while(~scanf("%s",c))
        {
            if(c[0]=='O')
            {
                scanf("%d",&a);
                v[a]=true;
                for(i=1;i<=n;i++)
                {
                    if(v[i]&&i!=a)
                        merge(i,a);
                }
            }
            else
            {
                scanf("%d%d",&a,&b);
                if(find(a)==find(b))
                    printf("SUCCESS\n");
                else printf("FAIL\n");
            }
        }
    }
}
*
#include<stdio.h>
int s[500005],dp[500005];
int search(int n,int k)
{
    int l=1,r=n,mid;
    while(l<=r)
    {
        mid=(l+r)/2;
        if(dp[mid]<k)
            l=mid+1;
        else
            r=mid-1;
    }
    return l;
}
int LIS(int n)
{
    int i,j,ans=1;
    dp[1]=s[1];
    for(i=2;i<=n;i++)
    {
        if(s[i]<=dp[1])
            j=1;
        else if(s[i]>dp[ans])
            j=++ans;
        else
            j=search(ans,s[i]);
        dp[j]=s[i];
    }
    return ans;
}
int main()
{
    int n,i,cas=1,x,y,ans;
    while(~scanf("%d",&n))
    {
        for(i=1;i<=n;i++)
            {scanf("%d%d",&x,&y);s[i]=y;}
        printf("Case %d:\n",cas++);
        ans=LIS(n);
        if(ans-1)
        printf("My king, at most %d roads can be built.\n",ans);
        else
        printf("My king, at most %d road can be built.\n",ans);
        printf("\n");
    }
    return 0;
}
*
#include<stdio.h>
#include<math.h>
#define N 100005
#define max(a,b) a>b?a:b;
#define min(a,b) a<b?a:b;
int s[N],maxsum[N][20],minsum[N][20];
int Rmax,Rmin;
void RMQ_init(int n)//预处理
{
    for(int j=1;j<=20;j++)//2^20也算是比较大的数了
        for(int i=1;i<=n;i++)
        if(i+(1<<j)-1<=n)
    {
        maxsum[i][j]=max(maxsum[i][j-1],maxsum[i+(1<<(j-1))][j-1]);
        minsum[i][j]=min(minsum[i][j-1],minsum[i+(1<<(j-1))][j-1]);
    }
}
int RMQ(int L,int R)
{
    int k=(int)(log(R-L+1.0)/log(2.0));//即L+2^k-1<=R
    Rmax=max(maxsum[L][k],maxsum[R-(1<<k)+1][k]);
    Rmin=min(minsum[L][k],minsum[R-(1<<k)+1][k]);
    return Rmax-Rmin;
}
int main()
{
    int n,t;
    scanf("%d%d",&n,&t);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&minsum[i][0]);//输入数据处理
        maxsum[i][0]=minsum[i][0];
    }
    RMQ_init(n);
    int l,r;
    while(t--)
    {
        scanf("%d%d",&l,&r);
        printf("%d\n",RMQ(l,r));
    }
}
*/
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    double s1[1002],s2[1002];
    int T=1;
    int t,n,i,j;
    scanf("%d",&t);
    while(t--)
    {
        int ans1=0,ans2=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%lf",&s1[i]);
        for(int i=0;i<n;i++)
            scanf("%lf",&s2[i]);
        sort(s1,s1+n);
        sort(s2,s2+n);
        int ks=0,js=0;
        while(ks<n&&js<n)
        {
            if(s2[ks]>s1[js])
            {
                ans2++;
                ks++;
                js++;
            }
            else
            {
                ks++;
            }
        }
        ans2=n-ans2;

        if(s1[0]>s2[n-1]) ans1=n;
        else if(s1[n-1]<s2[0]) ans1=0;
        else
        {
            int a=0,b=n-1;
            int p=0,q=n-1;
            while(a<n)
            {
                if(s1[a]>s2[p])
                {
                    ans1++;
                    a++;
                    p++;
                }
                else if(s1[a]<s2[p])
                {
                    a++;
                    q--;
                }
            }
        }
        printf("Case #%d: %d %d\n",T++,ans1,ans2);
    }
}
