#include <iostream>
#include <sstream>
#include <string.h>
#include <stdio.h>
#include <math.h>

using namespace std;

//#define MY_DEBUG

bool palindrome(const string& s)
{
    for (int i=0; i<s.size()/2; ++i)
        if (s[i] != s[s.size() - 1 - i])
            return false;
    return true;
}

bool check_fair(long long n)
{
    std::string str;
    std::stringstream strstream;
    strstream << n;
    strstream >> str;

    return palindrome(str);
}

int main(void)
{
    int cases = 0, loop = 0;
    long long min, max;
    
    cin >> cases;
    
#ifdef MY_DEBUG
    printf("=> cases=%d\n", cases);
#endif

    while (++loop <= cases)
    {
        int sqr_and_fair_count = 0;

        cin >> min >> max;
#ifdef MY_DEBUG
    printf("=> min=%d, max=%d\n", (int)min, (int)max);
#endif
        long long min_base = sqrt(min);
        long long max_base = sqrt(max);
        if (min_base*min_base != min)
            min_base++;
#ifdef MY_DEBUG
    printf("=> min_base=%d, max_base=%d\n", (int)min_base, (int)max_base);
#endif
        for (long long i=min_base; i<=max_base; i++)
        {
            long long ii = i*i;
            if ( check_fair(i) && check_fair(ii) )
            {
                sqr_and_fair_count++;
#ifdef MY_DEBUG
    printf("=> sqr_and_fair_count=%d, %d\n", sqr_and_fair_count, (int)ii);
#endif
            }
        }
        
        printf("Case #%d: %d", loop, sqr_and_fair_count);
        
        
        printf("\n");
    }

    return 0;
}
