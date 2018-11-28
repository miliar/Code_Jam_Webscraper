#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;


int N,J;


long long a[505];
long long F[505][12];
int n;


int check(int x)
{
    if(!(x&1)) return 0;
    if(!(x&(1<<15))) return 0;

    int c[20];
    for(int i=0;i<16;i++)
    {
        if(x&(1<<i)) c[i]=1;
        else c[i]=0;
    }

    for(int B=2;B<=10;B++)
    {
        long long cur=0;
        for(int i=15;i>=0;i--)
        {
            cur=cur*B+c[i];
        }
        int ok=0;
        long long p;
        for(long long i=2;i*i<=cur;i++)
        {
            if(cur%i==0)
            {
                ok=1;
                p=i; break;
            }
        }
        if(!ok) return 0;
        F[n][B]=p;
    }
    a[n++]=x;
    return 1;
}

void deal()
{
    N=16;
    J=50;

    n=0;

    int cur=0;
    for(int i=0;i<(1<<16);i++)
    {
        if(check(i))
        {
            cur++;
          //  printf("%d %d\n",i,cur);
        }

        if(cur==J) break;
    }

    for(int i=0;i<n;i++)
    {
        for(int j=15;j>=0;j--)
        {
            if(a[i]&(1<<j)) putchar('1');
            else putchar('0');
        }
        for(int j=2;j<=10;j++) printf(" %lld",F[i][j]);
        puts("");
    }
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("ans","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d:\n",i);
        deal();
    }
    return 0;
}
