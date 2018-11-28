#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<vector>

#define pii pair<int,int>
#define pll pair<LL,LL>
#define F first
#define S second
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

#define PI 4*arctan(1)

using namespace std;

int t,r,p,s,n,a[3],all,ep,er,es,id;
char ans[10005],s1[10005],s2[10005];
bool ch;

bool update(int rr,int pp,int ss)
{
    int sum=rr+pp+ss;
    if(sum==all)    return false;
    ep=pp+ss;
    es=ss+rr;
    er=rr+pp;
    return true;
}

void fil(int x,int dp)       //0=p  1=r  2=s
{
    if(dp==n)
    {
        if(x==0)        ans[id]='P';
        else if(x==1)   ans[id]='R';
        else            ans[id]='S';
        id++;
        return;
    }
    if(x==0)
    {
        fil(0,dp+1);
        fil(1,dp+1);
    }
    else if(x==1)
    {
        fil(1,dp+1);
        fil(2,dp+1);
    }
    else
    {
        fil(0,dp+1);
        fil(2,dp+1);
    }
}

void srt(int len)
{
    int g=all/len;
    for(int i=0;i<g;i+=2)
    {
        for(int j=0;j<len;j++)  s1[j]=ans[len*i+j];
        for(int j=0;j<len;j++)  s2[j]=ans[len*i+len+j];
        s1[len]=s2[len]='\0';
        if(strcmp(s1,s2)>0)
        {
            for(int j=0;j<len;j++)  ans[len*i+j]=s2[j];
            for(int j=0;j<len;j++)  ans[len*i+len+j]=s1[j];
        }
    }
}

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);

    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        id=0;
        ch=false;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        all=1<<n;
        ep=0;er=1;es=0;
        while(update(er,ep,es));       //rock wins
        if(er==r&&es==s&&ep==p)
        {
            ch=true;
            fil(1,0);
        }
        ep=1;er=0;es=0;
        while(update(er,ep,es));       //paper wins
        if(er==r&&es==s&&ep==p)
        {
            ch=true;
            fil(0,0);
        }
        ep=0;er=0;es=1;
        while(update(er,ep,es));        //scissor wins
        if(er==r&&es==s&&ep==p)
        {
            ch=true;
            fil(2,0);
        }
        if(!ch)
        {
            printf("Case #%d: IMPOSSIBLE\n",z);
            continue;
        }
        ans[all]='\0';
        for(int i=0;i<n;i++)    srt(1<<i);
        printf("Case #%d: %s\n",z,ans);
    }
    return 0;
}
