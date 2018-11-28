#include <iostream>
#include <cstdio>
using namespace std;

typedef long long ll;

int main()
{
    freopen("din.txt","r",stdin);
    freopen("dout.txt","w",stdout);
    int test_case, T;
    scanf("%d" , &T);
    for(test_case=1;test_case<=T;test_case++)
    {
        printf("Case #%d: " , test_case);
        int i,j;
        int K, C, S;
        scanf("%d %d %d" , &K, &C, &S);
        if(C*S<K)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        ll out;
        int tmp=(K-1);
        bool flag=false;
        for(i=0;i<S;i++)
        {
            if(flag)break;
            out=0LL;
            for(j=0;j<C;j++)
            {
                out=out*(ll)K;
                out=out+(ll)tmp;
                if(tmp==0)
                {
                    flag=true;
                    printf("%lld\n", out+1LL);
                    break;
                }
                tmp--;
            }
            if(!flag)
            {
                printf("%lld " , out+1LL);
            }
        }



    }

    return 0;
}
