#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int num;
bool ok;
struct node
{
    bool isword;
    int next[11];
    void init()
    {
        memset(next,0,sizeof(next));
        isword=false;
    }
}tree[100010];
void insert(char a[])
{
    int cou=0;
    int index=0;
    int len=strlen(a);
    for(int i=0; i<len; i++)
    {
        if(tree[index].next[a[i]-'0']==0)
        {
            tree[++num].init();//建立新节点
            tree[index].next[a[i]-'0']=num;//连接
            index=num;
        }
        else
        {
            cou++;
            index=tree[index].next[a[i]-'0'];
            if(tree[index].isword)
            {
                ok=false;
                return;
            }
        }
    }
    tree[index].isword=true;
    if(cou==len)
    ok=false;//统计是否为其他串的前缀
}
void dfs(char a[])
{
    insert(a);
    for (int i = 1; a[i]; ++i)
    {
        printf("%c",a[i]);
    }
}
char s[1009][1009];
int main()
{
    int cas;
    scanf("%d",&cas);
    for (int t = 1; t<= cas; ++t)
    {
        printf("Case #%d: ",t);
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i = 1; i <=n; ++i)
        {
            scanf("%s",s[i]);
            insert(s[i]);
        }
    }
    dfs(s[1]);
    cout<<endl;
    return 0;
}
