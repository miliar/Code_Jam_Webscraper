#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

#define eps 1e-8
#define MOD 10009
#define MAXN 1007
#define MAXM 100010
#define INF 99999999
using namespace std;
int equ,var;
int a[MAXN][MAXN];
int x[MAXN];

void init()
{
    memset(a,0,sizeof(a));
    memset(x,0,sizeof(x));
}
int Gauss()
{
    int max_r,col,k;
    for(k=0,col=0;k<equ&&col<var;k++,col++)
    {
        max_r=k;
        for(int i=k+1;i<equ;i++)
        {
            if(abs(a[i][col])>abs(a[max_r][col]))
                max_r=i;
        }
        if(a[max_r][col]==0)
        {
            x[col]=0;
            continue;
        }
        if(max_r!=k)
        {
            for(int j=col;j<var+1;j++)
                swap(a[k][j],a[max_r][j]);
        }
        for(int i=k+1;i<equ;i++)
        {
            if(a[i][col]!=0)
            {
                for(int j=col;j<var+1;j++)
                    a[i][j]^=a[k][j];
            }
        }
    }
    for(int i=k;i<equ;i++)
        if(a[i][col]!=0)
            return -1;//无解
    for(int i=var-1;i>=0;i--)
    {
        x[i]=a[i][var];
        for(int j=i+1;j<var;j++)
            x[i]^=(a[i][j]&&x[j]);
    }
    int cnt=0;
    for(int i=0;i<var;i++)
        cnt+=x[i];
    return cnt;
}
char str[MAXN];
int main()
{
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        int n;
        init();
        scanf("%s%d",str,&n);
        int k=strlen(str);
        var=k-n+1;
        equ=k;
        for(int i=0;i<equ;i++)
        {
            if(str[i]=='-')
                a[i][var]=1;
            else
                a[i][var]=0;
            for(int j=max(0,i-n+1);j<min(i+1,var);j++)
                a[i][j]=1;
        }
        int ans=Gauss();
        printf("Case #%d: ",kase);
        if(ans==-1) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}
