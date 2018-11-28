#include <iostream>
#include <vector>
using namespace std;

#define ull unsigned long long
#define ll long long

bool finish(bool digits[10], int n)
{
    bool finish = true;

    while (n != 0)
    {
        digits[n % 10] = true;
        n = n / 10;
    }

    for (int i = 0; i < 10; i++)
        finish = finish && digits[i];
    return finish;
}

string solve(int n)
{
    if (n == 0)
        return string("INSOMNIA");
    bool digits[10];
    for (int i = 0; i < 10; i++)
        digits[i] = false;

    ull tmp = n;
    while (!finish(digits, tmp))
        tmp += n;
    char tmpstr[100];
    return string(_itoa(tmp, tmpstr, 10));
}

void main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        int n;
        cin >> n;
        cout << "Case #" << i << ": " << solve(n).c_str() << endl;
    }
}