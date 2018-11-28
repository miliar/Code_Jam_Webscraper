#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <cstdint>
#include "prime_new.h"

using namespace std;

#define INT64 long long
#define INT128 __int128

int T;
int N, J;
int str[40];
int count = 0;
INT128 ans10_[15];
INT128 ans10[15];


INT128 isprime(INT128 n)
{ 
    for (int i = 0; prime[i] * prime[i] <= n; i++)
        if (n % prime[i] == 0)
            return prime[i];
    return -1;
}

INT128 getValue(INT128 b)
{
    INT128 now = 1;
    INT128 ans = 0;
    for (int i = 0; i < N; ++i)
    {
        ans += (INT128)str[i] * now;
        now *= b;
    }

    return ans;
}

void next()
{
    str[1]++;
    int t = 1;
    while(str[t] == 2)
    {
        str[t] = 0;
        str[t + 1]++;
        t++;
    }
}

void printAns()
{
    for (int i = N-1; i >=0 ; --i)
    {
        printf("%d", str[i]);
    }
    printf(" ");

    for (int i = 2; i <= 10; ++i)
    {
        printf("%lld ",ans10[i]);
    }
    printf("\n");

}

int main()
{

    scanf("%d", &T);
    
    for(int t = 1; t <= T; t++)
    {
        scanf("%d %d", &N, &J);

        str[0] = 1;
        str[N - 1] = 1;
        for (int i = 1; i < N-  1; ++i)
        {
            str[i] = 0;
        }

        printf("Case #%d:\n",t);

        while(count < J)
        {
            bool flag = true;
            for (int i = 2; i <= 10; ++i)
            {
                INT128 now = getValue(i);
                INT128 v = isprime(now);
                ans10[i] = v;
                ans10_[i] = now;
                if(v == -1)
                {
                    flag = false;
                    break;
                }
            }

            if(flag){
                count++;
                printAns();
            }

            next();
        }
    }
}