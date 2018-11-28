#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int MaxN = 107;

char str[MaxN];
int num[MaxN];

void Swap(int l,int r)
{
    int i,j,k;
    for (i=l,j=r; i<j; i++,j--)
    {
        k=num[i]; num[i]=1-num[j]; num[j]=1-k;
    }
    if(i==j) num[i] = 1-num[i];
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T,i,j,k,l,s; char str[MaxN];
    scanf("%d",&T);
    for (i=1; i<=T; i++)
    {
        scanf("%s",str+1);
        l=strlen(str+1); k=1; s=0;
        for (j=1; j<=l; j++)
            if(str[j]=='+') num[j]=1;
            else num[j]=0;
        for (j=l; j>=1; j--)
        {
            if(num[j]==k) continue;
            s++;
            if(num[1]==1-k) Swap(1,j);
            else k=1-k;
        }
        printf("Case #%d: %d\n",i,s);
    }
}