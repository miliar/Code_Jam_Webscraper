#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool isPalindrom(long long n)
{
    long long nn = n;
    long long reverse = 0;
    while(nn)
    {
        reverse *= 10;
        reverse += nn % 10;
        nn /= 10;
    }

    if (reverse == n)
        return true;

    return false;
}

long long process(long long A, long long B)
{
    int count = 0;
    for (long long i = /*floor(sqrt(B))*/B; i >= A; --i)
    {
        long long square = floor(sqrt(i));
        if (isPalindrom(i) && /*isPalindrom(i * i)*/ square * square == i && isPalindrom(square))
        {
//            cout << i << "    " << i * i << endl;
            ++count;
        }
    }

    return count;
}

int main(int argc, char **argv)
{
    ifstream ifs(argv[1]);

    int count;
    ifs >> count;

    for (int k = 0; k < count; k++)
    {
        long long A;
        ifs >> A;
        long long B;
        ifs >> B;

        cout << "Case #" << k + 1 << ": " << process(A, B) << endl;
    }
    return 0;
}
