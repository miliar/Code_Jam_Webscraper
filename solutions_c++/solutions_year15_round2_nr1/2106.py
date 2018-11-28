#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <utility>
#include <map>
#include <set>
#include <queue>
//#include <boost/math/common_factor_rt.hpp>

using namespace std;

typedef unsigned long long int ul;
#define forn(n,bound)       for(int n = 0; n < bound; n++)

unsigned long long int gcd(unsigned long long int a, unsigned long long int b)
{
    unsigned long long int t;
    while(b!=0)
    {
        t = b;
        b = a%b;
        a = t;
    }
    return a;
}

unsigned long long int lcm(unsigned long long int a, unsigned long long int b)
{
    return (a*b)/gcd(a,b);
}

unsigned int reversei(unsigned int i)
{
    unsigned int ret = 0;
    while(i>0)
    {
        ret += (i%10);
        i /= 10;
        if(i>0)
        ret *= 10;
    }
    return ret;
}

    unsigned int M[1000001];
int main(int argc, char *argv[])
{
    for(unsigned int i = 1; i <= 1000000; i++)
    {
        M[i] = i;
    }

    for(unsigned int i = 2; i <= 1000000; i++)
    {
        M[i] = min(M[i-1]+1, M[i]);

        if(reversei(i)<1000001)
            M[reversei(i)] = min(M[reversei(i)],M[i]+1);
        //if(i<100) cout << M[i] << endl;
    }
    int T;
    cin >> T;

    for(int tt = 1; tt<=T; tt++)
    {
        int N;
        cin >> N;
        cout << "Case #" << tt << ": " << M[N] << endl;
    }
    return 0;
}
