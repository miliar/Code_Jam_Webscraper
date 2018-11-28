#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
    int count;
    cin >> count;
    for (int i = 1; i < count + 1; ++i)
    {
        long long N;
        cin >> N;
        long long originalN = N;
        if (N == 0)
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }
        int bitmask = 0;
        while (bitmask != 1023)
        {
            long long n = N;
            while (n)
            {
                int remaining = n % 10;
                bitmask |= 1 << remaining;
                n = n / 10;
            }
            N += originalN;
        }
        N -= originalN;
        cout << "Case #" << i << ": " << N << endl;
    }
}
