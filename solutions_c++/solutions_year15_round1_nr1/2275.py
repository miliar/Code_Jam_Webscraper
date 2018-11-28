#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

int A[1050];

int main()
{
    freopen("A-large.in" , "r" , stdin);
    freopen("out.out" , "w" , stdout);

    int T , c = 0;
    scanf("%d" , &T);
    while(T--)
    {
        ++c;
        int N;
        scanf("%d" , &N);
        for(int i = 0;i < N;++i)
            scanf("%d" , &A[i]);

        long long ans1 = 0;
        for(int i = 1;i < N;++i)
            if(A[i] < A[i - 1])
                ans1 += (A[i - 1] - A[i]);

        long long ans2 = 0;
        long long mi = 0;
        for(int i = 1;i < N;++i)
            if(A[i] < A[i - 1])
                mi = max(mi , (A[i - 1] - A[i]) * 1LL);

        for(int i = 0;i < N - 1;++i)
            ans2 += min(A[i] * 1LL , mi);

        printf("Case #%d: %lld %lld\n" , c , ans1 , ans2);
    }
    return 0;
}
