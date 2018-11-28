#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.o", "w", stdout);
    int t,k,c,s,i;
    scanf("%d",&t);
    for(int ca=1; ca<=t; ca++)
    {
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d:",ca);
        for(i=1; i<=s; i++)
        {
            printf(" %d",i);
        }
        printf("\n");
    }


}
