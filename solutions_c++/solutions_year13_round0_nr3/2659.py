//
//  main.cpp
//  cj13_round0_c
//
//  Created by Peizhi Wu on 4/12/13.
//  Copyright (c) 2013 Peizhi Wu. All rights reserved.
//

#include <cmath>
#include <cstdio>

#define MAX 15

int check(unsigned long long m)
{
    int i, k, num[MAX];
    k = 0;
    while (m>0)
    {
        num[k] = m%10;
        m = m/10;
        k++;
    }
    k--;
    for (i = 0; 2*i<=k;i++)
        if (num[i]!=num[k-i])
            return 0;
    return 1;
}
int main()
{
    int T,TN, count;
    unsigned long long A, B, n, m;
    freopen("/Users/Peizhi/Documents/cpp/cj13_round0_c/cj13_round0_c/C-small-attempt1.in","r",stdin);
    freopen("/Users/Peizhi/Documents/cpp/cj13_round0_c/cj13_round0_c/C-small.txt","w",stdout);
    scanf("%d\n", &TN);
    for (T = 0; T<TN; T++)
    {
        scanf("%lld%lld\n", &A, &B);
        n = round(sqrt(double(A)));
        while (n*n<A) n++;
        count = 0;
        while (!check(n)) n++;
        m = n*n;
        while (m<=B)
        {
//            if (check(m))   printf("%lld\n", n*n);
            if (check(m)) count++;
            n++;
            while (!check(n)) n++;
            m =n*n;
        }
        printf("Case #%d: %d\n", T+1, count);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
