#include <cstdio>
#include <queue>
#include <vector>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#define INF -(1<<30)
#define INFP (1<<30)
#define pb push_back
#define mod 747474747
using namespace std;
char s[1010][1010];
char ss[1010][1010];
char d1[1010],d2[1010];
char c1[1010],c2[1010];
char c;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    bool flag1,flag2,flag3;
    int T,CASE=0,n,i,j,a,b;
    int cox,coy;
    scanf("%d",&T);
    while(T--)
    {
        cox=-1;
        coy=-1;
        memset(s,0,sizeof(s));
        memset(ss,0,sizeof(ss));
        memset(d2,0,sizeof(d2));
        memset(d1,0,sizeof(d1));
        memset(c1,0,sizeof(c1));
        memset(c2,0,sizeof(c2));
        flag1=false;
        flag2=false;
        flag3=false;

        n=4;
        a=0;
        b=0;
        for(i=0;i<4;i++)
        {
            scanf("%s",&s[i]);
            for(j=0;j<4;j++)
            {
                c=s[i][j];
                ss[j][i]=c;
                if(c=='T')  cox=i,coy=j;
                if(i==j)
                {
                    d1[a++]=c;
                }
                if(i+j==3)
                {
                    d2[b++]=c;
                }
                if(c=='.')  flag3=true;
            }
            c1[i]='X';
            c2[i]='O';
        }
        if(cox!=-1)
        {
            s[cox][coy]='X';
            ss[coy][cox]='O';
        }

        for(i=0;i<n;i++)
        {
            if(strcmp(c1,s[i])==0)  flag1=true;
            if(strcmp(c2,ss[i])==0)  flag2=true;
        }

        if(strcmp(d1,c1)==0)    flag1=true;
        if(strcmp(d2,c2)==0)    flag2=true;
        if(strcmp(d1,c2)==0)    flag2=true;
        if(strcmp(d2,c1)==0)    flag1=true;

        if(cox!=-1)
        {
            if(cox==coy)
            {
                d1[cox]='X';
                if(strcmp(d1,c1)==0)    flag1=true;
                d1[cox]='O';
                if(strcmp(d1,c2)==0)    flag2=true;
            }
            if(cox+coy==3)
            {
                d2[cox]='O';
                if(strcmp(d2,c2)==0)    flag2=true;
                d2[cox]='O';
                if(strcmp(d2,c1)==0)    flag1=true;
            }
        }
        printf("Case #%d: ",++CASE);
        if(flag1)   puts("X won");
        else if(flag2)  puts("O won");
        else if(flag3)  puts("Game has not completed");
        else puts("Draw");
    }
    return 0;
}
