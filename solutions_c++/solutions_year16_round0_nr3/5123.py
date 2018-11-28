#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

size_t pp[9][32];

inline size_t getDivisor(size_t number)
{
    for (size_t i = 2; i < sqrt(number); ++i)
    {
        if (number % i == 0) return i;
    }
    return 0;	
}

inline size_t getNum(size_t *jamcoin, size_t N, size_t base)
{
    size_t num = 1 + pp[base-2][N-1]; 
    for (size_t p(1); p < N-1; ++p)
    {
        if (jamcoin[p] == 1) num += pp[base-2][p];
    }
    return num;
}

inline void inc(size_t *jamcoin, size_t N)
{
    for (size_t p(1); p < N-1; ++p)
    {
        if (jamcoin[p] == 0) { jamcoin[p] = 1; break; }
        else jamcoin[p] = 0;
    }
}

int main(int argc, char** argv)
{
    cout << "Case #1:" << endl;

    const size_t N = 16;
    const size_t J = 50;
    for (size_t base(2); base <= 10; ++base)
        for (size_t p(0); p < N; ++p)
            pp[base-2][p] = pow(base, p);

    size_t jamcoin[N];
    jamcoin[0] = 1;
    jamcoin[N-1] = 1;
    for (size_t p(1); p < N-1; ++p) jamcoin[p] = 0;

    size_t d[9];
    //size_t num[9];
    for (size_t jj(0); jj < J; inc(jamcoin, N))
    {
        //for (size_t p(0); p < N; ++p) cout << jamcoin[N-p-1];
        bool foundPrime = false;
        for (size_t base(2); base <= 10; ++base)
        {
            //num[base-2] = getNum(jamcoin, N, base);
            size_t divisor = getDivisor(getNum(jamcoin, N, base));
            if (divisor == 0) { foundPrime = true; break;}
            d[base-2] = divisor;
        }
        //for (size_t base(2); base <= 10; ++base) cout << " " << num[base-2];
        //if (foundPrime) { cout << " prime" << endl; continue; }
        if (foundPrime) continue;

        for (size_t p(0); p < N; ++p) cout << jamcoin[N-p-1];
        for (size_t base(2); base <= 10; ++base) cout << " " << d[base-2];
        cout << endl;
        ++jj;
    }
}

