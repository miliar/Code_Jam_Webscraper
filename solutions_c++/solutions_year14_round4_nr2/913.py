#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MaxN = 10000;

int N;
int A[MaxN];

int lbig[MaxN], rbig[MaxN];


int main()
{
    int T;
    cin >> T;

    for(int c=0; c<T; c++)
    {
        cin >> N;
        for(int i=0; i<N; i++)
            cin >> A[i];

        memset(lbig, 0, sizeof(lbig));
        memset(rbig, 0, sizeof(rbig));

        // left big
        for(int i=0; i<N; i++)
            for(int j=0; j<i; j++)
                if(A[j] > A[i])
                    lbig[i]++;

        for(int i=0; i<N; i++)
            for(int j=i+1; j<N; j++)
                if(A[j] > A[i])
                    rbig[i]++;

        // max
        int maxidx = 0;
        int maxval = A[0];
        for(int i=1; i<N; i++)
            if(A[i] > maxval)
                maxval = A[i],
                maxidx = i;

        int minswap = 0;
        for(int i=0; i<N; i++)
            minswap += min(lbig[i], rbig[i]);


        /*for(int i=0; i<N; i++)
        {
            int swap1 = 0; //abs(maxidx - i);
            int swap2 = 0;
            int swap3 = 0;
            for(int j=0; j<i; j++)
                swap2 += lbig[j];
            for(int j=i+1; j<N; j++)
                swap3 += rbig[j];

            int total = swap1 + swap2 + swap3;

            if(total < minswap)
                minswap = total;
        }*/

        int result = minswap;

        printf("Case #%d: %d\n", c+1, result);
    }

    return 0;
}
