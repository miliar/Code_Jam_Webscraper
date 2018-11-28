#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<stdlib.h>
#include<ctype.h>
#include<utility>
#include<cmath>
using namespace std;
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#define eps 1e-7
#define ll long long
#define i64 __int64
#define INF 1000000005
#define pb push_back
#define sz(b) (int)b.size()
#define lson k<<1
#define rson k<<1|1
#define MOD 1000000007
#define CLR(t,x) memset(t,x,sizeof(t));
#define REP(k,x,y) for(k=x;k<y;k++)
#define N 1500000
char s1[200][55],s2[200][55],s[200][55];
int num[3005];
map<string,int> mp;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int cas,n,l,tt=1;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d%d",&n,&l);mp.clear();
        for(int i=0;i<n;i++) scanf("%s",s1[i]);
        for(int i=0;i<n;i++)
        {
            scanf("%s",s2[i]);
            mp[s2[i]]=1;
        }
        int S=(1<<l),ok,ans=INF;
        CLR(num,0);
        for(int i=0;i<S;i++) num[i]=num[i>>1]+(i&1);
        for(int i=0;i<S;i++)
        {
            ok=1;
            memcpy(s,s1,sizeof(s1));
            for(int j=0;j<n;j++)
                for(int k=0;k<l;k++)
                {
                    if(i&(1<<k))
                    {
                        if(s[j][k]=='0') s[j][k]='1';
                        else s[j][k]='0';
                    }
                }
            for(int j=0;j<n;j++) if(!mp[s[j]]) {ok=0;break;}
            if(ok) ans=min(ans,num[i]);
        }
        printf("Case #%d: ",tt++);
        if(ans==INF) puts("NOT POSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
