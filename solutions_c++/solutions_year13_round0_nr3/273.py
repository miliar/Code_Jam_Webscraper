#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<string>
#include<queue>
#define MAXN 64
#define INF 1<<30
///
using namespace std;

char paro[41552][105];

void init()
{
    freopen("init.txt","r",stdin);
    int k=0;
    char temp[128];
    while(scanf("%s",temp)==1)
    {
        strcpy(paro[k],temp);
        k++;
    }
    strcpy(paro[k],"20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000");
    fclose(stdin);
}

int solve1(char t[])
{
    int len=strlen(t);
    int pos;
    for(int i=0; i<41552; i++)
    {
        int curlen=strlen(paro[i]);
        if(curlen==len)
        {
            if(strcmp(paro[i],t)>=0)
            {
                pos=i;
                break;
            }
        }
        else if(curlen>len)
        {
            pos=i;
            break;
        }
    }
    return pos;
}

int solve2(char t[])
{
    int len=strlen(t);
    int pos;
    for(int i=0; i<41552; i++)
    {
        int curlen=strlen(paro[i]);
        if(curlen==len)
        {
            if(strcmp(paro[i],t)==0)
            {
                pos=i;
                break;
            }
            else if(strcmp(paro[i],t)>0)
            {
                pos=i-1;
                break;
            }
        }
        else if(curlen>len)
        {
            pos=i-1;
            break;
        }
    }
    return pos;
}

int main()
{
    init();
    freopen("C-large-2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases;
    scanf("%d",&cases);
    char temp[128];
    for(int c=1; c<=cases; c++)
    {
        int s,t;
        scanf("%s",temp);
        s=solve1(temp);
        scanf("%s",temp);
        t=solve2(temp);
        int ans=t-s+1;
        printf("Case #%d: %d\n",c,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
