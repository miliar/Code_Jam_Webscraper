#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>

using namespace std;

int main ()
{
    freopen ("outputB.txt", "w", stdout);
    freopen ("B-large.in", "r", stdin);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        string s;
        cin >> s;
        char c = s[0];
        int quantity = 0;
        for (int j = 0; j < s.size(); ++j)
        {
            if (c != s[j])
            {
                ++quantity;
                c = s[j];
            }
        }
        if (s[s.size() - 1] == '-')
            ++quantity;
        cout << "Case #" << i << ": " << quantity << endl;
    }
}

