#include <iostream>
#include <stdio.h>
#include <vector>

#define pb push_back

using namespace std;

typedef long long LL;

const LL p[] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};
const int sz = 39;

int solve(LL a, LL b) {
    int ret = 0;
    for(int i = 0; i < sz; i ++)
        if(a <= p[i] * p[i] && p[i] * p[i] <= b)
            ret ++;
    return ret;
}

int main()
{
    int t;
    LL a, b;

    scanf("%d", &t);
    for(int i = 1; i <= t; i ++) {
        scanf("%lld %lld", &a, &b);
        printf("Case #%d: %d\n", i, solve(a, b));
    }

    return 0;
}
