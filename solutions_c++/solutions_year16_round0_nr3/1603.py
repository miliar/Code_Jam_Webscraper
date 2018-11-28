#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <algorithm>
#include <set>

using namespace std;

long long base(long long n, long long b)
{
    if (n == 0)
        return n;
    return base(n / 10, b) * b + n % 10;
}

long long div(long long n)
{
    for (long long i = 2; i * i <= n; ++i)
    {
        if (n % i == 0)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    srand(time(NULL));
    ifstream in;
    in.open("C.in");
    ofstream out;
    out.open("C.out");
    int t;
    in >> t;
    set <long long> T;
    for (int i = 0; i < t; ++i)
    {
        int n, j;
        in >> n >> j;
        n /= 2;
        int s = 0;
        out << "Case #1: " << endl;
        while (j != s)
        {
            long long buf = 1;
            for (long long k = 0; k < n - 2; ++k)
            {
                buf *= 10;
                buf += rand() % 2;
            }
            buf *= 10;
            buf += 1;
            cout << buf << endl;
            vector <long long> A;
            bool divi = true;
            for (long long k = 2; k <= 10; ++k)
            {
                long long p = base(buf, k);
                int d = div(p);
                if (d == -1)
                {
                    divi = false;
                    break;
                }
                A.push_back(d);
            }
            if (divi && T.find(buf) == T.end())
            {
                T.insert(buf);
                out << buf << buf << " ";
                for (int k = 0; k < A.size(); ++k)
                {
                    out << A[k] << " ";
                }
                out << endl;
                ++s;
                cout << s << endl;
            }
        }
    }
    out.close();
    in.close();
    return 0;
}
