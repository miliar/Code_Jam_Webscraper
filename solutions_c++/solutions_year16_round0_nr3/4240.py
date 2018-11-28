#include<cstdio>
#include<map>
#include<cmath>
#include<cstring>
#include<iostream>
#include<cctype>
#include<queue>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
const int M=100005;
const LL mod=1e9+7;
const double eps=1e-8;
bool vis[1000005];
LL Cal(LL n)
{
    int m=sqrt(n+0.5);
    for(int i=2;i<=m;i++)
        if(n%i==0)
        {
           return n/i;
        }
    return -1;
}
LL Mak(string &s,int k)
{
    LL p=1,ans=0;
    int len=s.size();
    for(int i=len-1;i>=0;i--)
    {
        ans=ans+p*(s[i]-'0');
        p*=k;
    }
    return ans;
}
int main()
{
//    freopen("test1.in","r",stdin);
//    freopen("test2.out","w",stdout);
    int T,kase=1,m,n;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        printf("Case #%d:\n",kase++);
        memset(vis,false,sizeof(vis));
        int mi=(1<<(n-1))+1;
        int ma=1<<n;
        for(int i=mi;i<ma;i+=2)
        {
            bool ok=true;
            LL ans[10];
            int tot=0,k=i;
            string s="";
            while(k)
            {
                s+=(char)((k&1)+'0');
                k>>=1;
            }
            int L=0,R=n-1;
            while(L<R)
                swap(s[L++],s[R--]);
            tot=0;
            for(int j=2;j<=10;j++)
            {
                LL w=Mak(s,j);
                LL p=Cal(w);
                if(p==-1)
                {
                    ok=false;
                    break;
                }
                ans[tot++]=p;
            }
            if(ok)
            {
                cout<<s;
                for(int j=0;j<9;j++)
                    printf(" %lld",ans[j]);
                puts("");
                m--;
                if(m==0)
                    break;
            }
        }
    }
    return 0;
}
/*


*/
