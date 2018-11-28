#include<cstdlib>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<vector>
#define N 100
using namespace std;
int T,n,m;
int l,r,err;
char ma[N][N];
void init()
{
#ifndef ONLINE_JUDGE
    // freopen("ex.in","r",stdin);
    // freopen("ex.out","w",stdout);
#endif
}
void print2()
{
    // cout<<"l="<<l<<"  "<<"r="<<r<<endl;
    // cout<<".="<<m<<"  "<<"*="<<l*r-m<<endl;
    if(err)
    {
        puts("Impossible");return ;
    }
    for(int i=0;i<l;i++)
    {   for(int j=0;j<r;j++)
        {
            printf("%c",ma[i][j]);
        }
        puts("");
    }
}
void salve1()
{
    int cnt=1;
    ma[0][0]='c';
    for(int i=0;i<l;i++)
    {     
        for(int j=0;j<r;j++)
        {
            if(i+j==0)continue;
            if(cnt<m)
            {
                ma[i][j]='.';
                cnt++;
            }
            else 
            {
                ma[i][j]='*';
            }
        }
    }
}
void salveou()
{
    int cnt=2;
    ma[0][0]='c';
    ma[1][0]='.';
    for(int i=0;i<l;i++)
    {     
        if(i==0)
        {
            for(int j=1;j<r;j++)
            {
                if(cnt<m)
                {
                    ma[0][j]=ma[1][j]='.';
                    cnt+=2;
                }
                else 
                    ma[0][j]=ma[1][j]='*';
            }
            i++;
            continue;
        }
        if(m-cnt>=2*r&&i+1<l)
        {
            for(int j=0;j<r;j++)
            {
                ma[i][j]=ma[i+1][j]='.';
                cnt+=2;
            }
            i++;
        }
        else 
        {
            for(int j=0;j<r;j++)
            {
                if(j+1<r&&cnt<m)
                {
                    ma[i][j]=ma[i][j+1]='.';
                    cnt+=2;
                    j++;
                }
                else 
                    ma[i][j]='*';
            }
        }
    }
}
void salveji()
{
    int cnt=9;
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
        {
            ma[i][j]=(i+j==0?'c':'.');
        }
    for(int j=3;j<r;j++)
    {
        if(cnt<m)
        {
            ma[0][j]=ma[1][j]='.';
            cnt+=2;
        }
        else 
            ma[0][j]=ma[1][j]='*';
    }
    for(int i=3;i<l;i++)
    {
        if(cnt<m)
        {
            ma[i][0]=ma[i][1]='.';
            cnt+=2;
        }
        else 
            ma[i][0]=ma[i][1]='*';
    }
    for(int i=2;i<l;i++)
    {
        for(int j=(i==2)?3:2;j<r;j++)
        {
            if(cnt<m)
            {
                ma[i][j]='.';
                cnt++;
            }
            else 
            {
                ma[i][j]='*';
            }
        }
    }
}

int main()
{
    init();
    int ncase=0;
    scanf("%d",&T);
    while(T--)
    {
        err=0;
        printf("Case #%d:\n",++ncase);
        scanf("%d%d%d",&l,&r,&m);
        m=l*r-m;
        int minv=min(l,r);
        if(minv==1)
            salve1();
        else if(m==1||m==l*r)
            salve1();
        else if(minv==2)
        {
            if((((m&1))==0)&&m>=4)
                salveou();
            else 
                err=1;
        }
        else 
        {
            if((m&1)==0&&m>=4)
                salveou();
            else if((m&1)&&m>=9) 
                salveji();
            else
                err=1;
        }
        print2();
    }
    return 0;
}
