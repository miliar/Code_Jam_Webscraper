#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

typedef unsigned long long ull;

const char in[]  = "C-small-attempt0.in.txt";
const char out[] = "C.out.txt";

bool isPalindrome(ull num)
{
    ull tmp = num, inv = 0;
    
    while (tmp)
    {
        inv = inv*10 + (tmp % 10);
        tmp /= 10;
    }
    return (inv == num ? true : false);
}

int main(void)
{
    freopen(in, "rt", stdin);
    freopen(out, "wt", stdout);
    
    int T = 0;
    scanf("%d", &T);
    
    for (int casenum = 1; casenum <= T; ++casenum)
    {
        ull result = 0;
        ull begin, end;
        scanf("%llu%llu", &begin, &end);
        
        while ( begin <= end )
        {
            ull qrt = (ull)sqrt(begin);
            ull mod = begin%qrt;
            
            if ( !mod               &&
                 qrt * qrt == begin &&
                 isPalindrome(qrt)  &&
                 isPalindrome(begin) )
                ++result;

            ++begin;
        }
        
        printf("Case #%d: %llu\n", casenum, result);
    }
}
