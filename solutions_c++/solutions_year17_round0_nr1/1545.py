#include <iostream>
using namespace std;

int main()
{
    auto flip = [](auto begin, auto end)
    {
        for (auto it = begin; it != end; ++it)
        {
            if (*it == '-')
                *it = '+';
            else
                *it = '-';
        }
    };

    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas)
    {
        int k;
        string s;
        cin >> s >> k;
        
        int res = 0;
        for (int i = 0; i < s.size() - k + 1; ++i)
        {
            if (s[i] == '-')
            {
                ++res;
                flip(s.begin() + i, s.begin() + i + k);
            }
        }

        cout << "Case #" << cas << ": ";
        if (s == string(s.size(), '+'))
            cout << res << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}
