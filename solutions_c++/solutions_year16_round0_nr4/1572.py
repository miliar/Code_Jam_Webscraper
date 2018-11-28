#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#define ll long long
using namespace std;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt", "w",stdout);
#endif
    int T;
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        int k,c,s;
        cin>>k>>c>>s;
        printf("Case #%d:",ca);
        for(int i=1;i<=s;i++)
        {
            printf(" %d",i);
        }
        printf("\n");
    }
    return 0;
}
