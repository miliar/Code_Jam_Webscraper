#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <string>

using namespace std;

int main() 
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int TESTS;
    in >> TESTS;
    for (auto TEST = 1; TEST <= TESTS; ++TEST)
    {
        out << "Case #" << TEST << ": ";
        string S;
        in >> S;
        auto prev = S[0];
        int ans = 0;
        for (size_t i = 1; i < S.size(); ++i)
            if (S[i] != prev)
                prev = S[i], ++ans;
        out << ans + (S[S.size() - 1] == '-');
        out << endl;
    }
}