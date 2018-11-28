#include <iostream>
#include <cstdio>

using namespace std;

void solve(int ca)
{
    int k,c,s;
    cin>>k>>c>>s;
    printf("Case #%d:",ca);
    for(int i=1;i<=s;i++)
        printf(" %d",i);
    printf("\n");
    return ;
}

int main()
{
    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("D-small-attempt0.out","w",stdout);
    int t;
    cin>>t;
    for(int ca=1;ca<=t;ca++)
        solve(ca);
    return 0;
}
