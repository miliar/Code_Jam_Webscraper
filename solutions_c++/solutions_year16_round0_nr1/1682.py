#include <algorithm>
#include <cassert>
#include <complex>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <tuple>
#include <utility>
#include <vector>

#define REP(i,n) for(int i=0,nn=static_cast<int>(n);i<nn;i++)
#define REP_R(i,n) for(int i=static_cast<int>(n)-1;i>=0;i--)
#define ALL(v) v.begin(),v.end()
#define ALL_R(v) v.rbegin(),v.rend()
#define SZ(v) static_cast<int>(v.size())
template<typename T> inline T sqr(T a) { return a*a; }

uint16_t digits(int n)
{
    if (n == 0) return 1;
    uint16_t flags = 0;
    while (n > 0)
    {
        flags |= (1u << (n % 10));
        n /= 10;
    }
    return flags;
}

void solve()
{
    int N; std::cin >> N;
    if (N == 0)
    {
        std::cout << "INSOMNIA" << std::endl;
        return;
    }
    uint16_t flags = 0;
    int cur = N;
    while (flags != 0x3FF)
    {
        flags |= digits(cur);
        cur += N;
    }
    cur -= N;
    std::cout << cur << std::endl;
}

int main()
{
    int T; std::cin >> T;
    REP(t,T) { std::cout << "Case #" << (t+1) << ": "; solve(); }
}

