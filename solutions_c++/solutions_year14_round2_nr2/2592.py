#include <iostream>
#include <cstdint>
#include <cassert>

using namespace std;

uint64_t solve(uint64_t A, uint64_t B, uint64_t K)
{
    // cerr << A << "," << B << "," << K << endl;
    uint64_t counter = 0;
    for (uint64_t i = 0; i < A; ++i)
    {
        for(uint64_t j = 0; j < B; ++j)
        {
            uint64_t a = i & j;
            // cerr << i << "&" << j << " == " << a << " < " << K << " ? " << (a < K) << endl;
            if (a < K)
                counter++;
        }
    }
    // cerr << "counter == " << counter << endl;
    return counter;
}

void readAndSolve(const size_t caseNumber)
{
    uint64_t A, B, K;
    cin >> A >> B >> K;
    auto solution = solve(A,B,K);
    cout << "Case #" << caseNumber + 1 << ": " << solution << endl;
}

int main() {
    size_t T;
    cin >> T;
    for (size_t i = 0; i < T; ++i)
    {
        readAndSolve(i);
    }
}
