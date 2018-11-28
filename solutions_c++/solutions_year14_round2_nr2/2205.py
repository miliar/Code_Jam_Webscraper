#include<iostream>
#include<cstdio>
#define ull unsigned long long

using namespace std;

int main()
{
    int t,cas;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        printf("Case #%d: ",cas);
        int a,b,k,c=0,i,j;
        scanf("%d %d %d",&a,&b,&k);
        for(i=0;i<a;i++)
            for(j=0;j<b;j++)
                if((i&j)<k)
                    c++;
        printf("%d\n",c);
    }

    return 0;
}
