#include <iostream>
using namespace std;

void solve(const int testNo, const int N);
int digits(int N);
bool hasDigit(int digitMask, int d);

int main()
{
    int T;

    cin >> T;

    for(int ti = 1; ti <= T; ++ti)
    {
        int N;

        cin >> N;
        solve(ti, N);
    }

    return 0;
}

void solve(const int testNo, const int N)
{    
    if (N == 0)
    {
        cout << "Case #" << testNo << ": INSOMNIA" << endl;
        return;
    }

    static const int ALL_DIGITS = digits(1234567890);
    int index = 0;
    int mask = 0;
    
    do
    {
        ++index;
        mask |= digits(N * index);
    } while (mask != ALL_DIGITS);

    cout << "Case #" << testNo << ": " << N * index << endl;
}

bool hasDigit(int digitMask, int d)
{
    return digitMask & (1 << (d + 1));
}

int digits(int N)
{
    int mask = 0;

    do
    {
        int d = N % 10;        
        mask |= (1 << (d + 1) );
        N /= 10;
    } while(N);

    return mask;
}