#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    errno_t err;
    FILE* fin = nullptr;
    err = freopen_s(&fin, "B-large.in", "r", stdin);
    if (err != 0)
        fprintf(stdout, "error on freopen\n");

    FILE* fout = nullptr;
    err = freopen_s(&fout, "output.out", "w", stdout);
    if (err != 0)
        fprintf(stdout, "error on freopen\n");

    int T = 0;
    cin >> T;

    for (size_t i = 1; i <= T; ++i)
    {
        string str = "";
        cin >> str;
        int count = 0;
        while (str.find('-') != string::npos)
        {
            int i = 0;
            if (str[0] == '-')
            {
                while (str[i] == '-' && i < str.size())
                {
                    str[i] = '+';
                    ++i;
                }
            }
            else
            {
                while (str[i] == '+' && i<str.size())
                {
                    ++i;
                }
                if (i<str.size())
                {
                    for (int j = 0; j < i; j++)
                    {
                        str[j] = '-';
                    }
                }
            }
            ++count;
        }


        cout << "Case #" << i << ": ";
        cout << count << endl;
    }


}
