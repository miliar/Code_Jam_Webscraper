#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

set <long long> digits;

void uncover(long long number)
{
    long long i;
    while(number > 0)
    {
        i = number % 10;
        digits.erase(i);
        number /= 10;
    }
}

void fill_digits()
{
    digits.clear();
    for(long long i = 0; i < 10; i++)
        digits.insert(i);
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    long long k, i, n;
    cin >> k;
    vector <long long> req;
    req.resize(k);
    for(i = 0; i < k; i++)
    {
        cin >> req[i];
    }

    for(i = 0; i < k; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        if(req[i] == 0)
            cout << "INSOMNIA\n";
        else
        {
            fill_digits();
            long long now = req[i];
            while(not digits.empty())
            {
                uncover(now);
                now += req[i];
            }
            cout << now - req[i] << "\n";
        }
    }
    return 0;
}
