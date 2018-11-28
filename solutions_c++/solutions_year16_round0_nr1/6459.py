#include <string.h>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

namespace
{
class TestCase
{
public:
    TestCase(istream& is, ostream& os, ostream& logger)
        : in(is), out(os), logger(logger)
    {
    }
    void run();

private:
    template <typename T>
    auto read()
    {
        T i;
        in >> i;
        return i;
    }
    auto ri() { return read<int>(); };
    auto rd() { return read<double>(); };
    auto rs() { return read<string>(); };
    istream& in;
    ostream& out;
    ostream& logger;
};

void TestCase::run()
{
    // MAGIC goes here


    uint64_t n = ri();

    if (n == 0)
    {
        out << "INSOMNIA";
        return;
    }


    unsigned digits = 0;

    uint64_t i = 0u;
    while (digits != 0b1111111111u)
    {
        ++i;
        uint64_t x = n*i;
        while (x)
        {
            auto d = x % 10u;
            digits |= 1 << d;
            x /= 10u;
        }
    }

    out << i * n;


}
}

void run(istream& in, ostream& out, ostream& logger)
{
    int numCases;
    in >> numCases;
    //logger << "running " << numCases << " cases" << endl;
    out << fixed << setprecision(7);
    for (auto i = 0; i < numCases; ++i)
    {
        out << "Case #" << i + 1 << ": ";
        TestCase(in, out, logger).run();
        out << endl;
    }
}

int main() {
    run(cin, cout, cout);
}
