#include <bits/stdc++.h>
using namespace std;
char str[105];
int vis[1000005];
int ans;
void dfs(char *s,int d)
{
    //printf("%s %d\n",s,d);
    int flag=1,m=0;
    for(int i=0; s[i]; i++)
    {
        m<<=1;
        if(s[i]=='-')
        {
            flag=0;
            m|=1;
        }
    }
    if(vis[m]<=d)
        return ;
    vis[m]=d;
    if(flag)
    {
        ans=min(ans,d);
        return ;
    }
    for(int i=0; s[i]; i++)
    {
        char tmp[105];
        //printf("%s ",s);
        strcpy(tmp,s);
        reverse(tmp,tmp+i+1);
        //printf("%s ",tmp);
        for(int j=0; j<=i; j++)
            tmp[j]=(tmp[j]=='-'?'+':'-');
        //printf("%s\n",tmp);
        dfs(tmp,d+1);
    }
    //printf("%d\n",ans);
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cas,c=1;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf(" %s",str);
        int l=strlen(str);
        ans=0;
        int flag=1;
        while(flag)
        {
            flag=0;
            for(int i=l-1; i>=0; i--)
            {
                if(str[i]=='-')
                {
                    int j;
                    for(j=0; str[j]=='+'; j++);
                    if(j)
                    {
                        for(int k=0;k<j;k++)
                            str[k]='-';
                        ans++;
                    }
                    reverse(str,str+i+1);
                    for(int k=0; k<=i; k++)
                        str[k]=(str[k]=='-'?'+':'-');
                    ans++;
                    flag=1;
                }
            }
        }
        printf("Case #%d: %d\n",c++,ans);
    }
}
