#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;

int main() 
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    /*auto& in = cin;
    auto& out = cout;
    */int TESTS;
    in >> TESTS;
    for (auto TEST = 1; TEST <= TESTS; ++TEST)
    {
        out << "Case #" << TEST << ": ";
        vector<short> V(10, 0);
        uint64_t n;
        in >> n;
        auto i = 0;
        while (i < n * 100'000'000 && accumulate(V.begin(), V.end(), 0) < 10)
        {
            i += n;
            auto x = i;
            while (x)
                V[x % 10] = 1, x /= 10;
        }
        if (accumulate(V.begin(), V.end(), 0) != 10)
            out << "INSOMNIA";
        else
            out << i;
        out << endl;
    }
}