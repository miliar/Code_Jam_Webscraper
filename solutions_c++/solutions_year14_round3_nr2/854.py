#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int n,m;
int h[10];
char ch[101][101];
int len[101],sum,ans;
char cc[11111],tmp[11111];
void check()
{
     int ss=0,tt=0;
     for(int i=0;i<sum;i++)
         if(cc[i]!=cc[i+1])
             ss++;
     strcpy(tmp,cc);
     sort(tmp,tmp+sum);
     for(int i=0;i<sum;i++)
         if(tmp[i]!=tmp[i+1])
             tt++;
     if(ss==tt)ans++;
}
void dfs(int step)
{
     if(step==sum)
     {
         check();
         return;
     }
     for(int i=0;i<n;i++)
         if(h[i]==0)
         {
             h[i]=1;
             for(int j=0;j<len[i];j++)
                 cc[step+j]=ch[i][j];
             cc[step+len[i]]=0;
             dfs(step+len[i]);
             for(int j=0;j<len[i];j++)
                 cc[step+j]=0;
             h[i]=0;
         }
}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int tit,tot;
    for(scanf("%d",&tot),tit=1;tit<=tot;tit++)
    {
        ans=sum=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%s",tmp);
            int zz=strlen(tmp);
            int pos=0;
            for(int j=0;j<zz;j++)
                if(tmp[j]!=tmp[j+1])
                    ch[i][pos++]=tmp[j];
            len[i]=pos;
            sum+=len[i];
        }
        dfs(0);
        memset(ch,0,sizeof(ch));
        
        printf("Case #%d: %d\n",tit,ans);
    }
	return 0;
}
