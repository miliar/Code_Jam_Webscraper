#include<bits/stdc++.h>
using namespace std;

void solve(int x)
{
    printf("Case #%d:",x);
    int k,c,s;
    scanf("%d%d%d",&k,&c,&s);
    for(int i=1;i<=s;i++)
        printf(" %d",i);
    printf("\n");
}
int main()
{
    freopen("233.in","r",stdin);
    freopen("233.out","w",stdout);
    int t;scanf("%d",&t);
    for(int i=1;i<=t;i++)
        solve(i);
    return 0;
}
