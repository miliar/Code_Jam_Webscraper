#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int T,n,k,c[10000000],f[100],cnt; char s[100][100];
struct node {node *c[27];} *root[100];
void del(node *&p)
{
    if(!p) return;
    for(int i=0;i<27;++i) del(p->c[i]);
    delete p; p=0;
}
void ins(node *&p,char *s,int x,int l)
{
    if(!p) {p=new node(); ++cnt;}
    if(x==l) return;
    ins(p->c[s[x]],s,x+1,l);
}
int calc()
{
    cnt=0; for(int i=0;i<k;++i) del(root[i]);
    for(int i=0;i<n;++i) ins(root[f[i]],s[i],0,strlen(s[i]));
    return cnt;
}
void go(int x)
{
    if(x==n) ++c[calc()];
    else for(int i=0;i<k;++i) {f[x]=i; go(x+1);}
}
int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);
    scanf("%d",&T);
    for(int I=1;I<=T;++I)
    {
        scanf("%d%d",&n,&k); memset(c,0,sizeof(c));
        for(int i=0;i<n;++i) scanf("%s",s[i]);
        for(int i=0;i<n;++i)
            for(int j=0;j<strlen(s[i]);++j) s[i][j]-='A'-1;
        for(int i=0;i<n;++i) ins(root[0],s[i],0,strlen(s[i]));
        go(0); int x,y;
        for(int i=0;i<10000000;++i) if(c[i]) {x=i; y=c[i];}
        printf("Case #%d: %d %d\n",I,x,y);
    }
    return 0;
}
