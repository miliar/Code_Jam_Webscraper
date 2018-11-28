#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cfloat>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#define SIEVELIMIT 100000000
using namespace std;

bool isNotPrime[SIEVELIMIT];
vector<int> primes;
void sieve()
{
    isNotPrime[1] = true;
    for(int i=2; i < SIEVELIMIT; ++i)
    {
        if(isNotPrime[i])
            continue;

        primes.push_back(i);
        for(int j=(i<<1); j < SIEVELIMIT; j += i)
            isNotPrime[j] = true;
    }
}

int n, j;
bool tryPrinting(int digits[16])
{
    long long divisors[11] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    for(int b=2; b <= 10; ++b)
    {
        long long val = 0LL, sqrtVal;
        for(int i=n-1; i >= 0; --i)
            val = val * b + digits[i];
        sqrtVal = sqrt(val) + 1LL;
        for(int i=0; primes[i] < sqrtVal; ++i)
            if(!(val % primes[i]))
            {
                divisors[b] = primes[i];
                break;
            }
        if(!divisors[b])
            return false;
    }
    for(int i = n-1; i >= 0; --i)
        printf("%d", digits[i]);
    for(int b=2; b <= 10; ++b)
        printf(" %lld", divisors[b]);
    printf("\n");
    return true;
}

void recursiveGenerator(int digits[16], int val, int index)
{
    if(j > 0)
    {
        digits[index] = val;
        if(index == 1)
        {
            bool result = tryPrinting(digits);
            if(result)
            {
                --j;
            }
        }
        else
        {
            recursiveGenerator(digits, 0, index-1);
            if(j > 0)
                recursiveGenerator(digits, 1, index-1);
        }
    }
}

int main()
{
    int T;
    int digits[16];
    scanf("%d", &T);
    scanf("%d%d", &n, &j);

    sieve();
    printf("Case #1:\n");
 

    digits[0] = 1;
    digits[n-1] = 1;
    recursiveGenerator(digits, 0, n-2);
    if(j > 0)
        recursiveGenerator(digits, 1, n-2);

    return 0;
}
