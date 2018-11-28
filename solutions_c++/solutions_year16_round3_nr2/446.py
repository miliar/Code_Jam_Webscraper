#include<cstdio>
#include<algorithm>

using namespace std;

long long all;

int ans[60][60];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for ( int te = 1 ; te <= T ; te++ )
    {
        all = 1;
        int B;
        long long M;
        scanf("%d%lld",&B,&M);
        for ( int c=1 ; c<=B ; c++ )
        {
            for ( int d=c+1 ; d<=B-1 ; d++ )    ans[c][d] = 1;
            ans[c][B] = 0;
        }
        for ( int c=1 ; c<=B-2 ; c++ )  all*=2;
        printf("Case #%d: ",te);
        if ( all < M )
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("POSSIBLE\n");
            int poi = B;
            while( M > 0 )
            {
                all /= 2;
                if ( all == 0 ) all = 1;
                poi--;
                if ( M >= all )
                {
                    M -= all;
                    ans[poi][B] = 1;
                }
            }
            for ( int c=1 ; c<=B ; c++ )
            {
                for ( int d=1 ; d<=B ; d++ )    printf("%d",ans[c][d]);
                printf("\n");
            }
        }
    }
}
