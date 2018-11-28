#include <fstream>
#include <vector>
#include <cmath>
using namespace std;

unsigned long long getPow(int base, int exp)
{
    unsigned long long result = 1;
    for (int i = 1; i <= exp; i++)
        result *= base;
    return result;
}

unsigned long long convertToBase(unsigned long long n, int base)
{
    unsigned long long result = 0;
    int pos = 0;
    while (n)
    {
        if (n % 10 == 1)
            result += getPow(base, pos);
        n /= 10;
        pos++;
    }

    return result;
}

int getDivisor(unsigned long long n)
{
    if (n == 1)
        return -1;
    else if (n == 2)
        return 2;
    else if (n % 2 == 0)
        return 2;
    else
    {
        for (int i = 3; i <= sqrt(n); i += 2)
            if (n % i == 0)
                return i;
    }

    return -1;
}

unsigned long long getBinaryRepr(unsigned long long n)
{
    unsigned long long mask = 1ULL << 15, result = 0;
    while (mask)
    {
        if (mask & n)
            result = result * 10 + 1;
        else
            result = result * 10;
        mask >>= 1;
    }
    return result;
}

int main()
{
    int k = 0;
    bool prime;
    unsigned long long b = (1ULL << 15) + 1, a;

    ifstream f("input.in");
    ofstream g("output.out");
    int T, N, J;
    f >> T >> N >> J;
    g << "Case #1:\n";
    while (k < J)
    {
        a = getBinaryRepr(b);
        prime = false;
        vector<int> divisors;
        for (int i = 2; i <= 10 && !prime; i++)
        {
            int p = getDivisor(convertToBase(a, i));
            if (p == -1)
                prime = true;
            else
                divisors.push_back(p);
        }

        if (!prime)
        {
            k++;
            g << a << ' ';
            for (int j = 0; j < divisors.size(); j++)
                g << divisors[j] << ' ';
            g << '\n';
        }
        b += 2;
    }
    return 0;
}
