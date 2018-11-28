#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int Ans;
int a[110];
struct node
{
    int sz;
    char s[110];
};
node A[51000];
int cntt[210];
int Cntt=0;
void dfs(int now,int end,int Tot,int sum)
{
    if (now==end)
    {
        int p=0;
        memset(cntt,0,sizeof(cntt));
        for (int i=0;i<Tot;i++)
            for (int j=0;j<Tot;j++)
                cntt[i+j]+=a[i]*a[j];
        for (int k=(Tot-1)*2;k>=0;k--)
            A[Cntt].s[p++]=cntt[k]+'0';
        A[Cntt].sz=Tot*2-1;
        A[Cntt++].s[p]=0;
        Ans++;
        return;
    }
    int down=(now==0?1:0);
    for (int i=down;i<=3;i++)
    {
        a[now]=a[Tot-1-now]=i;
        if (now+1==end&&Tot%2==1)
        {
            if (sum+i*i<10) dfs(now+1,end,Tot,sum+i*i);
        }
        else
        {
            if (sum+i*i*2<10) dfs(now+1,end,Tot,sum+i*i*2);
        }
    }
}
char sa[200],sb[200];
int ck(char *s)
{
    int len=strlen(s),anss=0;
    for (int i=0;i<Cntt;i++)
    {
        if (A[i].sz>len) break;
        if (A[i].sz<len) anss++;
        else if (strcmp(A[i].s,s)<=0) anss++;
    }
    return anss;
}
int ck2(char *s)
{
    int len=strlen(s);
    if (len%2==0) return 0;
    for (int i=0;i<Cntt;i++)
    {
        if (A[i].sz>len) break;
        if (strcmp(A[i].s,s)==0) return 1;
    }
    return 0;
}
int main()
{
    freopen("C-large-2.in","r",stdin);
    freopen("C-large-2.out","w",stdout);
    Cntt=0;
    int Tot=0;
    for (int Len=1;Len<=25;Len++)
    {
        Ans=0;
        dfs(0,Len,Len*2-1,0);
        Tot+=Ans;
        Ans=0;
        dfs(0,Len,Len*2,0);
        Tot+=Ans;
    }
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        scanf("%s%s",sa,sb);
        printf("Case #%d: %d\n",ii,ck(sb)-ck(sa)+ck2(sa));
    }
    return 0;
}
