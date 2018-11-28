#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;
int s[90];
int n,k;
int id;
int T;
int main()
{
//    freopen("C.in","r",stdin);
//    freopen("C.out","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;++i)
    {
        int K,C,S;
        scanf("%d%d%d",&K,&C,&S);
        printf("Case #%d:",i);
        for(int j=1;j<=S;++j)
        {
            printf(" %d",j);
        }
        printf("\n");
    }
    return 0;
}