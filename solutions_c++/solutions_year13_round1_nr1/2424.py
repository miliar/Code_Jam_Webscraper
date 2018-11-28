//  Google Code Jam - Round 1A
//  Problem A
//  Submission by Zemblan (nainan.kovoor@gmail.com)
//


#include <cmath>
#include <iostream>

using namespace std;

typedef long long int Int;
typedef long double Real;


Int numRings(Real r, Real t)
{
    Real a = 2.0;
    Real b = (2.0 * r) - 1.0;
    Real c = -t;

    Real disc = (b * b) - (4.0 * a * c);
    Real val = (sqrt(disc) - b)/(2.0 * a);

    return floor(val);
}

void processTestCase(int caseNum)
{
    // Input
    Int r, t;
    cin >> r >> t;

    // Output
    cout << "Case #" << caseNum << ": " << numRings(r, t) << endl;
}


int main()
{
    int NTestCases;
    cin >> NTestCases;

    for (int t = 0; t != NTestCases; ++t) {
        processTestCase(t + 1);
    }

    return 0;
}
