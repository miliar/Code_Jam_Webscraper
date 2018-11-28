#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;
char s[20][20];
int ans1=0,ans2=0;
int a[20],cnt[20];
struct A
{
    int a[30];
}tree[100000];
int l=0;

void insert(int root, char s[])
{
    //cout<<root<<' '<<s<<endl;
    if (!(*s)) return;
    if (tree[root].a[*s-'A']==0)
    {
        tree[root].a[*s-'A']=++l;
        memset(tree[l].a,0,sizeof(tree[l].a));
    }
    //cout<<tree[root].a[*s-'A']<<' '<<s+1<<endl;
    insert(tree[root].a[*s-'A'], s+1);
}

void dfs(int now,int n,int m)
{
    if (now>n)
    {
        for (int i=1; i<=m; i++) if (cnt[i]==0) return;
        int ss=0;
        for (int i=1; i<=m; i++)
        {
            l=1; memset(tree[l].a,0,sizeof(tree[l].a));
            for (int j=1; j<=n; j++) if (a[j]==i) insert(1,s[j]+1);
            ss+=l;
            
        }
        if (ss>ans1) {ans1=ss; ans2=1;}
        else if (ss==ans1) ans2++;
        return;
    }
    for (int i=1; i<=m; i++)
    {
        a[now]=i;
        cnt[i]++;
        dfs(now+1,n,m);
        cnt[i]--;
    }
}

int main()
{
    int o,cas=0;
    scanf("%d",&o);
    while(o--)
    {
       
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i=1; i<=n; i++) scanf("%s",s[i]+1);
        ans1=0,ans2=0;
        dfs(1,n,m);
        printf("Case #%d: %d %d\n",++cas,ans1,ans2);
    }
}
