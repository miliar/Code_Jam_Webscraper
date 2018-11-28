#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool IsFull(vector<int>&a)
{
    for (int i = 0; i < 10; i++)
    {
        if (a[i] == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    errno_t err;
    FILE* fin = nullptr;
    err = freopen_s(&fin, "A-large.in", "r", stdin);
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
        long n = 0;
        unsigned long long temp = 0;
        string result = "";
        long res = 0;
        vector<int>a(10, 0);
        cin >> n;
        for (int j = 1; j <= 1000; j++)
        {
            temp = n*j;
            while (temp > 0)
            {
                int b = temp % 10;
                if (a[b] == 0)
                {
                    a[b] = 1;
                    if(IsFull(a))
                    {
                        res = n*j;
                        break;
                    }
                }
                temp /= 10;
            }
        }
        if (res != 0)
        {
            result.append(to_string(res));
        }
        else
        {
            result.append("INSOMNIA");
        }

        cout << "Case #" << i << ": ";
        cout << result << endl;
    }


}
