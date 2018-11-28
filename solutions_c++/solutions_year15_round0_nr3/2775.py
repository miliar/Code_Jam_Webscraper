#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<queue>
#include<list>
#include<map>
using namespace std;
#define gc getchar//_unlocked
#define pc(x) putchar(x)//_unlocked(x)
//#define pc(x) putchar_unlocked(x)

 int read_int() {
      char c = gc();
      while(c<'0' || c>'9') c = gc();
      int ret = 0;
      while(c>='0' && c<='9') {
        ret = 10 * ret + c - 48;
        c = gc();
      }
      return ret;
}

long long int lread_int() {
      char c = gc();
      while(c<'0' || c>'9') c = gc();
      long long int ret = 0;
      while(c>='0' && c<='9') {
        ret = 10 * ret + c - 48;
        c = gc();
      }
      return ret;
}
inline void scanint(int &x)
{
   register int c = gc();
   x = 0;
   int neg = 0;
   for(;((c<48 || c>57) && c != '-');c = gc());
   if(c=='-') {neg=1;c=gc();}
   for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
   if(neg) x=-x;
}
inline void scanllint(long long int &x)
{
   long long int c = gc();
   x = 0;
   long long int neg = 0;
   for(;((c<48 || c>57) && c != '-');c = gc());
   if(c=='-') {neg=1;c=gc();}
   for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
   if(neg) x=-x;
}
long long int gcd(long long int a,long long int b){
    if ( a==0 ) return b;
  return gcd ( b%a, a );
}
int mat[4][4]={1,2,3,4,2,-1,4,-3,3,-4,-1,2,4,3,-2,-1};
char st[10006];
int findi()
{
    int i,len,fin=1;
    len=strlen(st);
    for(i=0;i<len;i++)
    {
        if(st[i]=='i')
        {
            if(fin>0)
            {
                fin=mat[fin-1][1];
            }
            else
            {
                fin=-fin;
                fin=mat[fin-1][1];
                fin=-fin;
            }
        }
        if(st[i]=='j')
        {
            if(fin>0)
            {
                fin=mat[fin-1][2];
            }
            else
            {
                fin=-fin;
                fin=mat[fin-1][2];
                fin=-fin;
            }
        }
        if(st[i]=='k')
        {
            if(fin>0)
            {
                fin=mat[fin-1][3];
            }
            else
            {
                fin=-fin;
                fin=mat[fin-1][3];
                fin=-fin;
            }
        }
        if(fin==2)
        {
            return i+1;
        }
    }
    if(i==len)
        return -1;
}
int findj(int start)
{
    int i,len,fin=1;
    len=strlen(st);
    for(i=start;i<len;i++)
    {
        if(st[i]=='i')
        {
            if(fin>0)
            {
                fin=mat[fin-1][1];
            }
            else
            {
                fin=-fin;
                fin=mat[fin-1][1];
                fin=-fin;
            }
        }
        if(st[i]=='j')
        {
            if(fin>0)
            {
                fin=mat[fin-1][2];
            }
            else
            {
                fin=-fin;
                fin=mat[fin-1][2];
                fin=-fin;
            }
        }
        if(st[i]=='k')
        {
            if(fin>0)
            {
                fin=mat[fin-1][3];
            }
            else
            {
                fin=-fin;
                fin=mat[fin-1][3];
                fin=-fin;
            }
        }
        if(fin==3)
        {
            return i+1;
        }
    }
    if(i==len)
        return -1;
}
int findk(int start)
{
    int i,len,fin=1;
    len=strlen(st);
    for(i=start;i<len;i++)
    {
        if(st[i]=='i')
        {
            if(fin>0)
            {
                fin=mat[fin-1][1];
            }
            else
            {
                fin=-fin;
                fin=mat[fin-1][1];
                fin=-fin;
            }
        }
        if(st[i]=='j')
        {
            if(fin>0)
            {
                fin=mat[fin-1][2];
            }
            else
            {
                fin=-fin;
                fin=mat[fin-1][2];
                fin=-fin;
            }
        }
        if(st[i]=='k')
        {
            if(fin>0)
            {
                fin=mat[fin-1][3];
            }
            else
            {
                fin=-fin;
                fin=mat[fin-1][3];
                fin=-fin;
            }
        }
    }
    if(fin==4)
        return 1;
    else
        return -1;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        int x,l,i,j,o,ans=1;
        scanf("%d",&l);
        scanf("%d",&x);
        //printf("yes");
        scanf("%s",st);
        o=0;
        for(i=0;i<x;i++)
        {
            for(j=0;j<l;j++)
            {
                st[o++]=st[j];
            }
        }
        st[o++]='\0';
        l=findi();
        if(l<0)
            ans=0;
        else
            l=findj(l);
        if(l<0)
            ans=0;
        else
            l=findk(l);
        if(l<0)
            ans=0;
        if(ans==0)
            printf("Case #%d: NO\n",k);
        else
            printf("Case #%d: YES\n",k);
    }
    return 0;
}


