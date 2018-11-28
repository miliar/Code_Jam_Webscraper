#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<cmath>
#define MAXN 1005
using namespace std; 
struct node
{
    int son[26];
}p[1005];
char s[10][10];
int n,m,ans,Mx,a[10];
int getnum()
{
    int k,x,i,t,h,len,ans=0,num;
    for (t=1;t<=n;t++)
    {
          memset(p,0,sizeof(p));
          num=0;
          for (k=1;k<=m;k++)
            if (a[k]==t)
            {
                  len=strlen(s[k]),h=0;
                  for (i=0;i<len;i++)  
                  {
                         x=s[k][i]-'A';
                         if (!p[h].son[x]) p[h].son[x]=++num;
                         h=p[h].son[x];
                  }      
            }            
          ans+=num+1;
    }
    return ans;
}
void dfs(int x)
{
    int i,j,k;
    if (x>m)
    {
           for (i=1;i<=n;i++) //É¨n¸öÊ÷ 
           {
                 for (j=1;j<=m;j++) 
                    if (a[j]==i) break;
                 if (j>m) return;
           }
           k=getnum();
           if (k>Mx) Mx=k,ans=0;
           if (k==Mx) ans++;
           return;
    }
    for (i=1;i<=n;i++)
    {
           a[x]=i; 
           dfs(x+1);
    } 
    return;
}
int main()
{
    int T,cases,i;
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d",&T);
	for(cases=1;cases<=T;cases++)
	{ 
           scanf("%d%d",&m,&n);
           for (i=1;i<=m;i++) scanf("%s",s[i]);
           ans=Mx=0;
           dfs(1);
           printf("Case #%d: %d %d\n",cases,Mx,ans); 
	}
	return 0;
}


