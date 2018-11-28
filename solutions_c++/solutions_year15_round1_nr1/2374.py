#include <cmath>
#include <cstdio>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("mushroom_monster.txt", "w", stdout);
    int t, i;
    scanf("%d",&t);
    for(i=1; i<=t; i++)
    {
        int N;
        scanf("%d",&N);
        int A[N];
        for (int j=0; j<=N-1; j++)
        {
            scanf("%d",&A[j]);
        }
        int ans1 = 0;
        int ans2 = 0;
        for (int j=1; j<=N-1; j++)
        {
            if (A[j] < A[j-1])
            {
                ans1 += A[j-1] - A[j];
            }
        }
        int diff;
        int maxDiff = 0;
        for (int j=1; j<=N-1; j++)
        {
            if (A[j] < A[j-1])
            {
                diff = A[j-1] - A[j];
                if (diff > maxDiff)
                {
                    maxDiff = diff;
                }
            }
        }
        for (int j=0; j<=N-2; j++)
        {
            if (A[j] < maxDiff)
            {
                ans2 += A[j];
            }
            else
            {
                ans2 += maxDiff;
            }
        }
        printf("Case #%d: %d %d\n",i, ans1, ans2);
    }
    return 0;
}
