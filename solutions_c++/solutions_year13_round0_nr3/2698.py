#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

bool isPal(long long a)
{
    long long bit = 1;
    long long t = a;
    while (t > 9)
    {
        t /= 10;
        bit *= 10;
    }
    t = a;
    if (bit == 1)
        return true;
    int head, tail;
    while (bit > 1)
    {
        head = t / bit;
        tail = t % 10;
        if (head != tail)
            return false;
        t %= bit;
        t /= 10;
        bit /= 100;
    }
    return true;
}

bool isSquare(long long a)
{
    return sqrt(a) == int(sqrt(a));
}

int main()
{
    ofstream fout;
    fout.open("out.out", ios::out);
    int i;
    int n, t;
    t = 0;
    cin >> n;
    while (t < n)
    {
        ++t;
        int a, b;
        cin >> a >> b;
        int cnt = 0;
        for (i = a; i <= b; ++i)
        {
            if (isPal(i) && isSquare(i))
            {
                int t = sqrt(i);
                if (isPal(t))
                {
                    ++cnt;
                    continue;
                }
            }
        }
        fout << "Case #" << t << ": " << cnt << endl;
    }
    return 0;
}
