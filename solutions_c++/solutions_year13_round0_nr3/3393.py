#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <sstream>

using namespace std;

bool isInt(double d)
{
    return (d == (int)(d * 10 / 10));
}

bool isPalindrome(int number)
{
    stringstream ss;
    ss << number;
    string right = ss.str();
//    cout << "strRight: " << strRight << endl;
    const char *reverse = string(right.rbegin(), right.rend()).c_str();
//    cout << "strReverse: " << reverse << endl;

    return (strcmp(reverse, right.c_str()) == 0);
}

int countFairAndSquare(int low, int high)
{
    int count = 0;
    for (int i = low; i <= high; ++i) {
        if (isPalindrome(i)) {
            double squareRoot = sqrt(i);
            if (isInt(squareRoot)) {
                if (isPalindrome(squareRoot)) ++count;
            }
        }
    }
    return count;
}

int main()
{
    ifstream si;
    si.open("C-small-attempt0.in", fstream::in);

    char ct[12] = { 0 };
    si >> ct;

    int t = 0;
    t = atoi(ct);
    //cout << t << endl;
    for (int i = 0; i < t; ++i) {
        char clow[12] = { 0 };
        char chigh[12] = { 0 };
        si >> clow >> chigh;
        int low = atoi(clow);
        int high = atoi(chigh);
        cout << "Case #" << i+1 << ": " << countFairAndSquare(low, high) << endl;
    }
    si.close();

    return 0;
}

