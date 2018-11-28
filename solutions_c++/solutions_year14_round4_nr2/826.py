#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

long long A[2000];

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T, n;
    scanf("%d", &T);
    for(int cas = 1 ; cas <= T ; cas++)
    {
        scanf("%d", &n);
        for(int i = 0 ; i < n ; i++)
        {
            scanf("%lld", &A[i]);
        }

        int ans = 0;
        int lt = 0, rt = n - 1;
        while(lt < rt)
        {
            int idx = lt;
            for(int i = lt + 1 ; i <= rt ; i++)
                if(A[idx] > A[i])idx = i;
            if((idx - lt) < (rt - idx))
            {
                ans += (idx - lt);
                for(int j = idx ; j > lt ; j--)
                    swap(A[j], A[j - 1]);
                lt++;
            }
            else
            {
                ans += (rt - idx);
                for(int j = idx ; j < rt ; j++)
                    swap(A[j], A[j + 1]);
                rt--;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
