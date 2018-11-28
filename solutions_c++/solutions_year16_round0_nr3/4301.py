#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

long long T;

void convert(long long n, long long base, string& str)
{
    if (n / base != 0) {
        convert(n / base, base, str);
    }
    str += to_string(n % base);
}

long long reconvert(string str, long long base)
{
    long long k = 1;
    long long value = 0;
    for (long long i = str.length() - 1; i >= 0; --i)
    {
        if (str[i] == '1') value += k;
        k *= base;
    }
    return value;
}

vector<string> jamcoins;
vector< vector<int> > dividers;

int main()
{
    ifstream in("C-small-attempt0.in");
    in >> T;

    ofstream out("C-small-attempt0.out");

    for (long long t = 0; t < T; ++t)
    {
        long long N, J;
        in >> N >> J;

        for (long long i = pow(2, N - 1) + 1; i < pow(2, N); i += 2)
        {
            string str;
            convert(i, 2, str);

            bool is_jamcoin = true;
            vector<int> div;
            for (long long j = 2; j <= 10; ++j)
            {
                long long value = reconvert(str, j);
                for (long long k = 2; k < 1000; ++k)
                {
                    if (value % k == 0)
                    {
                        div.push_back(k);
                        break;
                    }
                }
            }

            if (div.size() == 9)
            {
                jamcoins.push_back(str);
                dividers.push_back(div);
            }

            if (jamcoins.size() == J) break;
        }

        out << "Case #" << t + 1 << ":" << endl;
        for (int i = 0; i < jamcoins.size(); ++i)
        {
            out << jamcoins[i] << " ";
            for (int j = 0; j < dividers[i].size(); ++j)
                out << dividers[i][j] << " ";

            out << endl;
        }
    }

    in.close();
    out.close();

    return 0;
}