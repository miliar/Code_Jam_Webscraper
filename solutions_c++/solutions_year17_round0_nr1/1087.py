#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

const int MAXN=10086;
int T;
int kase=0;
int k;
int len;
int a[MAXN];
int ans;

inline void case_init()
{
    char t=getchar();
    while(t!='-'&&t!='+') t=getchar();
    for(len=0;t=='-'||t=='+';t=getchar()) a[++len]=((t=='+')?1:0);
    scanf("%d",&k);
}
inline void case_solve()
{
    ans=0;
    for(int i=1;i<=len-k+1;++i)
    {
    //    for(int j=1;j<=len;++j) printf("%d ",a[j]);
    //    printf("\n");
        if(a[i]==1) continue;
//        printf("%d   ",i);
        for(int j=0;j<k;++j) a[j+i]^=1;
        ++ans;

//        for(int j=1;j<=len;++j) printf("%d ",a[j]);
//        printf("\n");
    }
    for(int i=1;i<=len;++i) if(!a[i]) ans=-1;
    printf("Case #%d: ",++kase);
    if(ans!=-1) printf("%d\n",ans);
    else printf("IMPOSSIBLE\n");
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    for(scanf("%d",&T);T;--T)
    {
        case_init();
        case_solve();
    }
    return 0;
}
