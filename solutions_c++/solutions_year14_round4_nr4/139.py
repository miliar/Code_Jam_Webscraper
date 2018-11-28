#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
using namespace std;
#define FO(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)

int n,m;
char s[10][15];

struct trieNode
{
    trieNode* n[27];
    trieNode()
    {
        memset(n,0,sizeof (trieNode*)*27);
    }
};

void init()
{
    scanf("%d%d",&n,&m);
    for (int i=0;i<n;i++)scanf("%s",s[i]);
}
int gp[10];
void clearRoot(trieNode* nw)
{
    for (int i=0;i<26;i++)if (nw->n[i]!=NULL)
        clearRoot(nw->n[i]);
    delete nw;
}
int countNode()
{
    int ret=0;
    for (int k=1;k<=m;k++)
    {
        //printf("  k = %d\n",k);
        bool first=true;
        int cnt=0;
        trieNode* root = new trieNode();
        for (int i=0;i<n;i++)if (gp[i]==k)
        {
            if (first)cnt++,first=false;
            int len=strlen(s[i]);
            trieNode* tmp=root;
            for (int j=0;j<len;j++)
            {
    //printf("YES\n");
                if (tmp->n[s[i][j]-'A']==NULL)
                    tmp->n[s[i][j]-'A']=new trieNode(),cnt++;
                tmp=tmp->n[s[i][j]-'A'];
            }
        }
        clearRoot(root);
        ret+=cnt;
    }
    //printf("ret = %d\n",ret);
    return ret;
}

int ans=0,ans2=0;
void dfs(int nw)
{
    //printf("%d\n",nw);
    if (nw==n)
    {
        int tmp=countNode();
        if (tmp>ans)ans=tmp,ans2=1;
        else if (tmp==ans)ans2++;
        return ;
    }
    for (int i=1;i<=m;i++)
    {
        gp[nw]=i;
        dfs(nw+1);
    }
}
void solve()
{
    ans=0,ans2=0;
    dfs(0);
    printf("%d %d\n",ans,ans2);
}
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int Q;
    scanf("%d",&Q);
    for (int i=1;i<=Q;i++)
    {
        init();
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}

