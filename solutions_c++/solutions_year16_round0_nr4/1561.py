#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;



int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int t,k,c,s;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        printf("Case #%d: ",cas);
        scanf("%d%d%d",&k,&c,&s);
        long long n=1;
        for (int i=1;i<=c;++i) n*=k;
        if (s==k)
            for (int i=1;i<=s;++i)
                printf("%I64d%c",1+n/k*(i-1),i==s?'\n':' ');
    }
    return 0;
}
