#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<stack>
using namespace std;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out2.out", "w", stdout);
#endif
    int T;
    int k,c,s;
    scanf("%d",&T);
    int u=0;
    while(T--)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",++u);
        for(int i=1;i<=k;i++)
        {
            if(i==1) printf("%d",i);
            else printf(" %d",i);
        }
        printf("\n");
    }
    return 0;
}
