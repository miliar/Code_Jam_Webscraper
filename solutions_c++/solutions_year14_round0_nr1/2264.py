#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<map>
#include<cstdlib>
using namespace std;

int _bit[1<<17];
void init()
{
    memset(_bit,0,sizeof(_bit));
    for(int i=1;i<(1<<17);i++)
    {
        int temp = i;
        while(temp)
        {
            _bit[i] += temp&1;
            temp>>=1;
        }
    }
}
int getNum(int _bitNum)
{
    for(int i=1;i<32;i++)
    {
        if(_bitNum&(1<<i))
        return i;
    }
    return 0;
}
int getS()
{
    int line,num;
    int S=0;
    scanf("%d",&line);
    for(int i=1;i<=4;i++)
    {
        for(int j=0;j<4;j++)
        {
            scanf("%d",&num);
            if(i==line)
            {
                S |= (1<<num);
            }
        }
    }
    return S;
}
void solve()
{
    int S1 = getS();
    int S2 = getS();
    int S = S1 & S2;
   // printf("%d & %d = %d\n",S1,S2,S);
    if(_bit[S]==0)
    {
        printf("Volunteer cheated!\n");
    }
    else if(_bit[S]==1)
    {
        printf("%d\n",getNum(S));
    }
    else
    {
        printf("Bad magician!\n");
    }
}

int main()
{
    freopen("a.out","w",stdout);
    freopen("a.in","r",stdin);
    init();
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
