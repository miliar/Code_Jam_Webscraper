//Google Code Jam Round 1B 2014 - Problem B.
//https://code.google.com/codejam

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
using namespace std;

int main()
{
    freopen ("b_output.txt","w",stdout);

    int T, A, B, K, ans;
    scanf("%d", &T);

    for(int testCase = 1; testCase <= T; testCase++)
    {
        printf("Case #%d: ", testCase);
        ans = 0;

        scanf("%d %d %d", &A, &B, &K);

        for(int i = 0; i < A; i++)
        {
            for(int j = 0; j < B; j++)
            {
                int tmp = i & j;
                if(tmp < K)
                    ans ++;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}
