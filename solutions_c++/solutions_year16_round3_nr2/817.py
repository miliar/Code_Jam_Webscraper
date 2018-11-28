#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

typedef long long ll;

int main()
{
    freopen("bin.txt","r",stdin);
    freopen("bout.txt","w",stdout);
    int test_case, T;
    scanf("%d" , &T);
    for(test_case=1;test_case<=T;test_case++)
    {
        printf("Case #%d: " , test_case);
        int i, j;
        int B;
        ll M;
        scanf("%d" , &B);
        scanf("%lld" , &M);
        ll tmp=1LL;
        for(i=0;i<B-2;i++)
        {
            tmp*=2LL;
        }
        int X[B][B];
        if(M>tmp)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        else if(M==tmp)
        {

        printf("POSSIBLE\n");
            for(i=0;i<B;i++)
            {
                for(j=0;j<B;j++)
                {
                    if(j>i)
                    {
                        printf("1");
                    }
                    else
                    {
                        printf("0");
                    }
                }
                printf("\n");
            }
            continue;

        }

        printf("POSSIBLE\n");
        for(i=0;i<B;i++)
        {
            for(j=0;j<B;j++)
            {
                if(i>=j)
                {
                    printf("0");
                }
                else if(j<B-1)
                {
                    printf("1");
                }
                else if(i!=0)
                {
                    printf("%d" , M%2);
                    M/=2LL;
                }
                else
                {
                    printf("0");
                }
            }
            printf("\n");
        }


    }

    return 0;
}
