#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int inverse(int x) {
    int inv = 0;

    while (x > 0) {
        inv = (inv * 10) + (x % 10);
        x /= 10;
    }

    return inv;
}

int fairAndSquareNumbersIn(int a, int b) {
    int counter = 0;

    int num = floor(sqrt(a));
    if (pow(num, 2) < a) {
        ++num;
    }

    int square = pow(num, 2);

    while (square <= b) {
        if ((square == inverse(square)) && (num == inverse(num))) {
            ++counter;
        }
        ++num;
        square = pow(num, 2);
    }

    return counter;
}

int main()
{
    ifstream inStream("C-small-attempt0.in");
//    ostream& outStream = cout;
    ofstream outStream("C-small-attempt0.out");

    int numCases;
    int a;
    int b;
    inStream >> numCases;

    for (int i = 1; i <= numCases; ++i) {
        inStream >> a;
        inStream >> b;
        int solution = fairAndSquareNumbersIn(a, b);
        outStream << "Case #" << i << ": " << solution << endl;
    }

    inStream.close();
    outStream.close();

    return 0;
}

