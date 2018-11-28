#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
typedef long long ull;
ull ans[12];
ull judge(ull n,ull base,ull bit)
{
    ull nn=0;
    for(ull i=bit-1;i>=0;i--)
        if(n&(1<<i))
            nn=nn*base+1;
        else
            nn=nn*base;
    for(ull i=2;i*i<=nn;i++)
        if(nn%i==0)
            return i;
    return -1;
}
bool solve(ull n,int bit)
{
    n=n*2+1;
    n=n+(1<<(bit-1));
    for(int base=2;base<=10;base++)
    {
        ans[base]=judge(n,base,bit);
        if(ans[base]==-1)
            return false;
    }
    for(int i=bit-1;i>=0;i--)
        if(n&(1<<i))
            printf("1");
        else
            printf("0");
    for(int base=2;base<=10;base++)
        printf(" %lld",ans[base]);
    printf("\n");
    return true;
}
int main()
{
    int n,j;
    scanf("%*d%d%d",&n,&j);
    n-=2;
    int tot=0;
    printf("Case #1:\n");
    for(int i=0;i<(1<<n)&&tot<j;i++)
        if(solve(i,n+2))
            ++tot;
    return 0;
}
