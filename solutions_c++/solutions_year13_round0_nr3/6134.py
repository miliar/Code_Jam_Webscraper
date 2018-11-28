#include <iostream>
#include <map>
#include <cmath>
#include <string>
using namespace std;

static map<long long, int> M;

bool check(long long n)
{
    if (M[n] == 1)
        return true;
    else if (M[n] == -1)
        return false;

    string str1 = to_string(n);
    string str2 = to_string(n*n);
    

    if ((str1 == string(str1.rbegin(), str1.rend())) && (str2 == string(str2.rbegin(), str2.rend())))
    {
        M[n] = 1;
        return true;
    }
    else
    {
        M[n] == -1;
        return false;
    }
}

int main()
{
    int T;
    long long A, Art;
    long long B, Brt;
    long long cnt;

    M[1] = 1;

    cin >> T;

    for (int i = 1; i <= T; i++)
    {
        cin >> A >> B;
        cnt = 0;

        Art = (long long)(sqrt(double(A)));
        while (Art * Art < A)
            Art++;

        Brt = (long long)(sqrt(double(B)));
        while (Brt * Brt > B)
            Brt--;

        for (long long j = Art; j <= Brt; j++)
        {
            if (check(j))
            {
                cnt++;
            }
        }

        cout << "Case #" << i << ": " << cnt << endl;
    }

    return 0;
}
