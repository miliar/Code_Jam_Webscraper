#include <fstream>
#include <vector>

using namespace std;

bool isPrime (long long n, long long &d)
{
    for (d = 2; (d * d) <= n && d < n; d++)
        if ((n % d) == 0)
            return false;
    return true;
}

bool isOK (int n, vector<int> &vec)
{
    for (int base = 2; base <= 10; base++)
    {
        long long c = 0, p = 1;
        for (int k = 0; k < 16; k++, p *= base)
            if ((n >> k) & 1)
                c += p;
        long long d = 1;
        if (!isPrime(c, d))
            vec.push_back(d);
        else
            return false;
    }
    return true;
}

int main()
{
    ofstream cout("output.out");
    int NI = 14, J = 50, j = 0;
    cout << "Case #1: \n";
    for (int N = 0; N < (1 << 14), j < J; N++)
    {
        int n = (1 << 14) + N;
        n = (n << 1) + 1;
        vector<int>vec;
        if (isOK(n, vec))
        {
            for (int k = 15; k >= 0; k--)
                if ((n >> k) & 1)
                    cout << 1;
                else
                    cout << 0;
            cout << ' ';
            for (int i = 0; i < vec.size(); i++)
                cout << vec[i] << ' ';
            cout << '\n';
            j++;
        }
    }
    return 0;
}
