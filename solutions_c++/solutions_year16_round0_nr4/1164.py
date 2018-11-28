#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
using namespace std;

unsigned long long kk[200];

unsigned long long dfs(unsigned long long c, unsigned long long pos, unsigned long long k, unsigned long long origin)
{
    if ( c == 0 )
        return pos;
    pos = k * (pos - 1) + origin;
    return dfs(c-1,pos,k,origin);
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    int _, ca=1;
    scanf("%d", &_);
    while (_--)
    {
        unsigned long long k,c,s;
        scanf("%llu%llu%llu", &k,&c,&s);
        printf("Case #%d: ",ca++);
        for (unsigned long long i = 1 ; i <= k ; i++ )
        {
            printf("%llu", dfs(c-1,i,k,i));
            if ( i < k )
                printf(" ");
        }
        puts("");
    }
    return 0;
}
