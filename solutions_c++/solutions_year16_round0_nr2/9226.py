#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

bool check(string &a)
{
    bool f = true;
        for (int j = 0; j < a.length(); j++)
            if (a[j] == '-')
            {
                f = false;
                break;
            }
    return f;
}

void swp(string &a)
{
    char c = a[0];
    int i = 0;
    while (a[i] == c)
    {
        a[i] = ((a[i] == '+') ? '-' : '+');
        i++;
    }
}

int main()
{
    int t, i, j, r, f, n, k;
    string s;

    ifstream cin("B-large.in");
    ofstream cout("output.txt");

    cin >> t;

    for (i = 1; i <= t; i++)
    {
        cin >> s;
        k = 0;
        while (!check(s)) {
            swp(s);
            k++;
        }
        cout << "Case #" << i << ": " << k << "\n";
    }

    return 0;
}
