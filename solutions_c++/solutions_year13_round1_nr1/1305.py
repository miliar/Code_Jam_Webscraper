#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <sstream>

using namespace std;

long long solve()
{
    long long M, N;
    long long i=1;
    scanf("%lld %lld", &M, &N);
    long long temp = N;
    for(;;)
    {
        long long temp2 = (M+2*(i-1)+1)*(M+2*(i-1)+1)-(M+2*(i-1))*(M+2*(i-1));
        if (temp>=temp2) {
            temp-=temp2;
            i++;
        } else break;
    }
    return (i-1);
}

int main()
{
    freopen("AA-small-attempt1.in", "r", stdin);
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++)
    {
        printf("Case #%d: %lld\n", t, solve());
    }
    return 0;
}
