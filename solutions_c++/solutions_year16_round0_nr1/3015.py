#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

void Calc(int n)
{
    int x,y,s;
    for (x=n,s=0; s<(1<<10)-1; x+=n)
    {
        y=x;
        while(y)
        {
            s|=(1<<(y%10));
            y/=10;
        }
    }
    printf("%d",x-n);
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,n,i;
    scanf("%d",&T);
    for (i=1; i<=T; i++)
    {
        scanf("%d",&n);
        printf("Case #%d: ",i);
        if(n==0) printf("INSOMNIA");
        else Calc(n);
        printf("\n");
    }
    return 0;
}
