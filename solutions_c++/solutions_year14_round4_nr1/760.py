#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#define MAXN 10005
using namespace std;
int s[MAXN]; 
bool used[MAXN];
int main()
{
       int T,cases,n,x,i,j,ans;
       freopen("A-large (1).in","r",stdin);
       freopen("output.txt","w",stdout);
       scanf("%d",&T);
       for (cases=1;cases<=T;cases++)
       {
              scanf("%d%d",&n,&x);
              for (i=1;i<=n;i++) scanf("%d",&s[i]); 
              memset(used,false,sizeof(used));
              sort(s+1,s+1+n);
              ans=0;
              j=n;
              for (i=1;i<=n;i++)
                if (!used[i])
                {
                      ans++;
                      while (s[i]+s[j]>x && j>i) j--; 
                      used[i]=used[j]=true;
                      if (i!=j) j--;
                } 
              printf("Case #%d: %d\n",cases,ans);
       }
       return 0;
}
