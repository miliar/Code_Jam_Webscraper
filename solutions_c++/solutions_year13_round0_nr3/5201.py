#include <iostream>
#include <string>
#include <sstream>
#include <cstdio>
#include <cmath>
using namespace std;

inline bool isPal(unsigned long long x)
{
    ostringstream strm;
    strm << x;
    string a(strm.str());
    string b(a.rbegin(), a.rend());
    return a == b;
}

int main(void)
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        int count = 0;
        unsigned long long A, B;
        cin >> A >> B;
        unsigned long long sqrA = (unsigned long long)sqrt((double)A);
        for(unsigned long long j = sqrA; j * j <= B; ++j)
        {
            if(j * j < A)
                continue;
            if(isPal(j) && isPal(j*j))
                ++count;
        }
        printf("Case #%d: %d\n", i, count);
    }
    return 0;
}
