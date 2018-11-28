#include <iostream>
#include<stdio.h>
using namespace std;
int flg[100];
bool dog(__int64 p)
{

    while(p)
    {
        flg[p%10]=1;
        p=p/10;
    }
    for(int i=0;i<=9;i++)
        if (flg[i]==0) return false;
    return true;
}
int main()
{
    int n,x;
    freopen("111.txt","r",stdin);
    freopen("222.txt","w",stdout);
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&x);
        if (x==0)
        {
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        for(int j=0;j<=9;j++)
            flg[j]=0;
        for(int j=1;;j++)
            if (dog(j*x))
            {
                printf("Case #%d: %d\n",i,x*j);
                break;
            }
    }
    return 0;
}
