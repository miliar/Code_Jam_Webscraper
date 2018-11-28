#include <cstdio>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <deque>
#include <cmath>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    long long T, N, A[1000+10], minA, rate, minB;
    scanf("%lld", &T);
    for(int caseNum=1; caseNum<=T; caseNum++)
    {
        minA=0;
        rate=0;
        minB = 0;
        scanf("%lld", &N);
        long long big, last, item;
        scanf("%lld", &big);
        last = big;
        A[0] = big;
        for(int i=1; i<N; i++)
        {
            scanf("%lld", &A[i]);
            if(big > A[i])
            {
                minA += big-A[i];
                big = A[i];
            }
            big = max(big, A[i]);

            if(last > A[i])
                rate = max(rate, last-A[i]);
            last = A[i];
        }
        if(rate > 0)
        {
            for(int i=0; i<N-1; i++)
            {
                minB += min(A[i], rate);
            }
        }
        printf("Case #%lld: %lld %lld\n", caseNum, minA, minB);
    }
    return 0;

}
