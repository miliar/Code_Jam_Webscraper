#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int T;

bool is_digits[10] = { false };
int cnt = 0;

void clear()
{
    for (long long i = 0; i < 10; ++i) { is_digits[i] = false; }
    cnt = 0;
}

void check_digits(long long value)
{
    do
    {
        long long digit = value - (value / 10) * 10;
        if (!is_digits[digit])
        {
            is_digits[digit] = true;
            cnt++;
        }
        value /= 10;
    } while (value != 0);
}

int main()
{
    ifstream in("A-large.in");
    in >> T;

    ofstream out("A-large.out");

    for (int t = 0; t < T; ++t)
    {
        long long N;
        in >> N;

        if (N == 0)
        {
            out << "Case #" << t + 1 << ": " << "INSOMNIA" << endl;
        }
        else
        {
            long long k = 0;
            long long value = N;
            while (cnt != 10)
            {
                value = N * (++k);
                check_digits(value);
            }
            out << "Case #" << t + 1 << ": " << value << endl;
        }

        clear();
    }

    in.close();
    out.close();

    return 0;
}