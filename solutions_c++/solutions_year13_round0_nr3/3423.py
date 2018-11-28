#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

class FairSquare {
public:
    FairSquare(long, long);
    ~FairSquare();
    bool isFair(long);
    int check();

private:
    long A;
    long B;
    long sqrtA;
    long sqrtB;
};

FairSquare::FairSquare(long X, long Y)
{
    A = X;
    B = Y;
    sqrtA = ceil(sqrt(A));
    sqrtB = sqrt(B);
}

FairSquare::~FairSquare()
{
}

bool FairSquare::isFair(long X)
{
    stringstream ss;
    ss << X;
    string s = ss.str();

    for (int i = 0; i <= s.size() / 2; i++) {
        if (s[i] != s[s.size() - i - 1]) {
            return false;
        }
    }

    return true;
}

int FairSquare::check()
{
    int count = 0;
    for (int i = sqrtA; i <= sqrtB; i++) {
        if(isFair(i) && isFair(i * i))
            count++;
    }

    return count;
}

int main()
{
    ifstream inf("C-small-attempt1.in");
    if (!inf.is_open())
        cout << "Error when open file\n";

    ofstream of("result.out");
    int T;
    inf >> T;
    int S = T;
    while (T > 0) {
        of << "Case #" << S - T + 1 << ": ";
        long A, B;
        inf >> A;
        inf >> B;
        FairSquare f(A, B);
        of << f.check() << endl;
        T--;
    }

    return 0;
}
