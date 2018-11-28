#include <iostream>
#include <string>
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

int solve(string s)
{
    char last = s[0];
    int result = 1;
    for (int i = 1; i < s.length(); i++)
    {
        if (last != s[i])
        {
            last = s[i];
            result++;
        }
        last = s[i];
    }
    if (last == '+')
        result--;
    return result;
}

void main()
{
    int t;
    cin >> t;
    string tmp;
    getline(cin, tmp);
    for (int i = 1; i <= t; i++)
    {
        string s;
        getline(cin, s);
        cout << "Case #" << i << ": " << solve(s) << endl;
    }
}