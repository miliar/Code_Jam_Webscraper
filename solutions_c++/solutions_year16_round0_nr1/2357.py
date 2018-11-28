/*
* @Author: Comzyh
* @Date:   2016-04-09 20:42:55
* @Last Modified by:   Comzyh
* @Last Modified time: 2016-04-09 20:49:49
*/

#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int T;
long long N;
bool dig[10];
int main()
{
    scanf("%d", &T);
    for (int TT = 1; TT <= T; TT++)
    {
        scanf("%lld", &N);
        memset(dig, 0, sizeof(dig));
        printf("Case #%d: ", TT);
        if (N == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int ndig = 0;
        for (long long i = N;; i += N)
        {
            long long n = i;
            while (n)
            {
                ndig += dig[n % 10] == false;
                dig[n % 10] = true;
                n /= 10;
            }
            if (ndig == 10)
            {
                printf("%lld\n", i);
                break;
            }
        }
    }
    return 0;
}