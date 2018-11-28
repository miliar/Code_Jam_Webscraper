#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<deque>
#include<bitset>
#define ll __int64
#define inf 0x7FFFFFFF
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
int now;
int r,c;
char ch[55][55];
int get(int row,int column)
{
    int sum=0;
    for(int i=row-1;i<=row+1;i++)
    for(int j=column-1;j<=column+1;j++)
    {
        if(i>=1&&i<=r&&j>=1&&j<=c)
        {
            if(ch[i][j]=='*')
            {
                sum++;
                ch[i][j]='.';
            }
        }
    }
    return sum;
}
int print(int column)
{
    if(now<0) return -1;
    if(now==0) return 0;
    for(int i=1;i<=r;i++)
    {
        if(ch[i][column]!='0')
        {
            if(ch[i][column]=='*') now--;
            ch[i][column]='0';
            now-=get(i,column);
            if(now==0) return 0;
            else if(now<0) return -1;
        }
    }
    for(int i=1;i<=c;i++)
    {
        if(ch[column][i]!='0')
        {
            if(ch[column][i]=='*') now--;
            ch[column][i]='0';
            now-=get(column,i);
            if(now==0) return 0;
            else if(now<0) return -1;
        }
    }
}
int main()
{
    int i,j,k;
    int n,m,t;
    freopen("C-small-attempt3.in","r",stdin);freopen("C-small-output.txt","w",stdout);
    scanf("%d",&t);for(int tcase=1;tcase<=t;tcase++)
    //while(scanf("%d",&n)!=EOF)
    {
        scanf("%d%d%d",&r,&c,&m);
        printf("Case #%d:\n",tcase);
        if(!(m<=r*c-4||m==r*c-1||min(r,c)==1))
        {
            printf("Impossible\n");
            continue;
        }
        for(i=1;i<=r;i++)
        for(j=1;j<=c;j++)
        {
            ch[i][j]='*';
        }
        if(m==r*c-1)
        {
            ch[1][1]='c';
            for(i=1;i<=r;i++){
            for(j=1;j<=c;j++)
            {
                printf("%c",ch[i][j]);
            }puts("");}
            continue;
        }
        if(m==r*c-9&&min(r,c)>=3)
        {
            for(i=1;i<=3;i++)
            for(j=1;j<=3;j++)
            {
                ch[i][j]='.';
            }
            ch[1][1]='c';
            for(i=1;i<=r;i++){
            for(j=1;j<=c;j++)
            {
                printf("%c",ch[i][j]);
            }puts("");}
            continue;
        }
        now=r*c-m;
        int column=1;
        int judge=0;
        for(i=1;i<=min(r,c);i++)
        {
            if(print(i)==-1)
            {
                judge=1;
                break;
            }
        }
        if(judge==1)
        {
            printf("Impossible\n");
        }
        else
        {
            ch[1][1]='c';
            for(i=1;i<=r;i++){
            for(j=1;j<=c;j++)
            {
                if(ch[i][j]=='0') printf(".");
                else printf("%c",ch[i][j]);
            }puts("");}
        }
    }
    fclose(stdin);
    fclose(stdout);
}
