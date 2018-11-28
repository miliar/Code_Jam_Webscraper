#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("resD.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int K,C,S;
        scanf("%d%d%d",&K,&C,&S);
        printf("Case #%d:",ca);
        for(int i=1;i<=S;i++)printf(" %d",i);
        printf("\n");
    }
    return 0;
}
