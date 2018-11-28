#include<stdio.h>
#include<string.h>
int n;
char s[2005];
bool vis[2005];
FILE* fi = fopen("A-large.in","r");
FILE* fo = fopen("lastwordlarge.txt","w");
void print(int x)
{
    if(x<0) return ;
    int now = 0,i;
    for(i=0;i<=x;i++)
    {
        if(s[i]>=s[now])
        {
            now = i;
        }
    }
    vis[now] = true;
    fprintf(fo,"%c",s[now]);
    print(now-1);
}
main()
{
    int time,i,num = 1;
    fscanf(fi,"%d",&time);
    while(time--)
    {
        fscanf(fi," %s",s);
        n = strlen(s);
        memset(vis,0,sizeof(vis));
        fprintf(fo,"Case #%d: ",num++);
        print(n-1);
        for(i=0;i<n;i++) if(!vis[i]) fprintf(fo,"%c",s[i]);
        fprintf(fo,"\n");
    }
}
