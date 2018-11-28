#include <bits/stdc++.h>

using namespace std;

int main()
{
    int casos;
    scanf("%d",&casos);
    for(int caso=1;caso<=casos;caso++)
    {
        int c,s;
        long long k;
        printf("Case #%d:",caso);
        scanf("%lld %d %d",&k,&c,&s);
        long long num=1;
        for(int i=1;i<c;i++)
            num*=k;
        for(int i=0;i<s;i++)
        {
            printf(" %lld",num*i+1);
        }
        printf("\n");
    }
    return 0;
}