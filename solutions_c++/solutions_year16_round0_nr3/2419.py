#include <iostream>
#include <cmath>
#include <vector>
#include <bitset>

using namespace std;

typedef long long ll;

ll powers[10][16];

int main()
{
    for (int i = 0; i < 16; i++)
        powers[i][0] = 1;
    for (int i = 2; i <= 10; i++)
    {
        for (int j = 1; j < 16; j++)
        {
            powers[i][j] = powers[i][j - 1] * i;
        }
    }

    ll bits = 1 + (1 << 15);
    ll max = 1 << 16;
    int count = 0;
    cout << "Case #1:" << endl;
    while (bits < max && count < 50)
    {
        vector<int> div;
        bitset<16> b(bits);
        for (int i = 2; i <= 10; i++)
        {

            ll number = 0;
            for (int j = 0; j <= 15; j++)
            {
                if (bits & 1 << j)
                    number += powers[i][j];
            }

            bool TooHigh = true;
            for (int i = 2; i < 10000; i++)
            {
                if (number % i == 0)
                {
                    div.push_back(i);
                    TooHigh = false;
                    break;
                }
            }
            if (TooHigh)
                goto next;
        }
        cout << b << " ";
        for (int i = 0; i < div.size(); i++)
        {
            cout << div[i];
            if (i != div.size() - 1)
                cout << " ";
        }
        cout << endl;
        count++;
    next:
        bits += 2;
    }
    return 0;
}