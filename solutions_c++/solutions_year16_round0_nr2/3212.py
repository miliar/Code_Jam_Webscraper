#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<time.h>
#include<cmath>
#include<vector>
#include <iomanip>
#define PB(u)  push_back(u);
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
#define mminf(u)  memset(u,0x3f,sizeof(u))
using namespace std ;
#define MAX 105
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);

char s[MAX];
int len ;

int findd()
{
    for(int i=len-1;i>=0;i--)
    {
        if(s[i]=='-')
            return i ;
    }
    return -1 ;
}

void fun(int n)
{
    for(int i=0;i<=n;i++)
    {
        if(s[i]=='-')  s[i]='+';
        else s[i]='-';
    }
    reverse(s,s+n+1);
}


int fin()
{
    for(int i=0;i<len;i++)
    {
        if(s[i]!='+')
            return  i;
    }
}


int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T ;
    cin>>T;
    int cas=1;
    while(T--)
    {
        scanf(" %s",s);
        len=strlen(s);
        int ans=0;
        while(1)
        {
            int i=findd();
            if(i==-1)  break ;
            if(s[0]=='-')
            {
                int i=findd();
                if(i==-1)  break ;
                ans++;
                fun(i);
            }
            else
            {
                int j=fin();
                fun(j-1);
                ans++;
            }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}


