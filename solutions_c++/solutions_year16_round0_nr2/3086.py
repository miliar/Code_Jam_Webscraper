#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
const int maxn=1010;

int n,A[maxn],f[maxn][2];
char s[maxn];

void init()
{
     scanf("%s",s+1);
     n=strlen(s+1);
     for(int i=1;i<=n;i++) A[i]=(s[i]=='+');
}

void work()
{
     f[0][0]=f[0][1]=0;
     for(int i=1;i<=n;i++)
         if(A[i])
         {
            f[i][1]=f[i-1][1];
            f[i][0]=f[i-1][1]+1;
         }else
         {
            f[i][1]=f[i-1][0]+1;
            f[i][0]=f[i-1][0];
         }
     printf("%d\n",f[n][1]);
}

int main()
{
    int TT;
    scanf("%d",&TT);
    for(int i=1;i<=TT;i++)
    {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}

