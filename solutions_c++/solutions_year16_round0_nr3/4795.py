#include <bits/stdc++.h>
#define LL long long
using namespace std;
const int maxTest = 100;
int num[50],a[60],N;
LL ans[11];

LL Random(LL n)
{
    return (LL)((double)rand()/RAND_MAX*n+0.5);
}

LL Modular_Exp(LL a, LL b, LL n) // a^b mod n
{
    LL ans;
    if(b == 0) return 1;
    if(b == 1) return a%n;
    ans = Modular_Exp(a, b/2, n);
    ans = ans*ans%n;
    if(b%2) ans = ans*a%n;
    return ans;
}

bool Miller_Rabbin(LL n)
{
    for(int i=1; i<=maxTest; i++)
    {
       LL a = Random(n-2)+1;
       if(Modular_Exp(a, n-1, n) != 1)return false;;
    }
    return true;
}
LL get(LL n, int k)
{
    int i=0;
    LL s=1,ans=0;
    while(n)
    {
        num[++i] = n % 2;
        n/=2;
    }
    for (int j=1;j<=i;j++)
    {
        if (num[j] == 1) ans += s;
        s*=k;
    }
    return ans;
}

bool vis[1000+10];
void init()
{
    N=0;
    memset(vis,0,sizeof vis);
    for (int i=2;i<=1000;i++){
        if (!vis[i])
        {
            if (N<=50) a[++N] = i;
            for (int j=i*i;j<=1000;j+=i) vis[j]=1;
        }
    }
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    init();
    int t,cas=0,n,k;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&k);
        printf("Case #%d:\n",++cas);
        LL L =(LL) (1<<(n-1));
        LL R = (LL)(1<<n)-1;
        //printf("%lld %lld\n",L,R);
        int cut = 0;
        for (LL i=L;i<=R;i++)
        {
            int b=i;
            if (b%2==0) continue;
            bool flag=1;
            memset(ans,0,sizeof ans);
            for (int j=2;j<=10;j++)
            {
                LL tp=get(i,j);
                //printf("%lld %lld\n",i,tp);
                Miller_Rabbin(tp);
                //printf("%lld\n",tpm);
                if (!Miller_Rabbin(tp))
                {
                    for (int ii = 1;ii<=N;ii++)
                    if (tp%a[ii] == 0)
                    {
                        ans[j] = a[ii];
                        break;
                    }
                }
                else {
                    flag=0;
                    break;
                }
                if (ans[j] == 0) {flag=0; break;}
            }
            if (flag)
            {
                cut++;
                for (int j=n-1;j>=0;j--)
                {

                    if (b & (1<<j)) printf("1");
                    else printf("0");
                }
                for (int j=2;j<=10;j++) printf(" %lld",ans[j]);//printf(" %lld,",get(i,j));}
                printf("\n");
            }
            if (cut == k) break;
        }
    }
    return 0;
}
