//#pragma comment(linker, "/STACK:102400000,102400000")
#include <bits/stdc++.h>

#define inf 0x3f3f3f3f
#define PI  acos(-1.0)
#define eps 1e-8
#define LL  long long
#define PB  push_back
#define MP  make_pair
#define PQ  priority_queue
#define MII map<int,int>::iterator
#define MLL map<LL,LL>::iterator
#define PII pair<int,int>
#define SI  set<int>::iterator
#define SL  set<LL>::iterator
#define MSI map<string,int>::iterator
#define IN  freopen("in.txt","r",stdin);
#define OUT freopen("out.txt","w",stdout);
#define BUG printf("bug************bug************bug\n");

#define MEM(a,b) memset(a,b,sizeof(a))
#define M_SI     multiset<int>::iterator

using namespace std;
const int maxn=1000+10;
int a[maxn],dp[maxn];
void work()
{
    int t,cas=0,c,n,v;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&c,&n,&v);
        for (int i=1;i<=n;i++) scanf("%d",&a[i]);
        MEM(dp,0); dp[0]=1;
        for (int i=1;i<=n;i++)
        {
            for (int j=v;j-a[i]>=0;j--)
            {
                if (dp[j-a[i]]) dp[j]=1;
            }
        }
        //for (int i=1;i<=v;i++) printf("%d %d\n",i,dp[i]);
        int ans=0;
        for (int i=1;i<=v;i++)
        {
            if (!dp[i])
            {
                ans++;
                for (int j=v;j>=i;j--) if (dp[j-i]) dp[j]=1;
            }
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return;
}

int main()
{
    IN;
    OUT;
    work();
    return 0;
}
