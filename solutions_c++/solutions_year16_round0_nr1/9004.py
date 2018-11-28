#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int sheep(int a)
{
    bool d[10];
    char w[10];
    int j = 1;
    memset(d, 0, sizeof(d));
    while (true)
    {
        long long b = a;
        b *= j;
        j++;
        sprintf(w, "%d", b);
        string s = string(w);
        for (int i = 0; i < s.length(); i++)
        {
            d[s[i] - '0'] = true;
        }
        long long g = 0;
        for (int i = 0; i < 10; i++)
        {
            if (d[i])
                g += 1;
            else
                g -= 1000;
        }
        if (g == 10)
        {
            return b;
            break;
        }
    }
}

int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t, n;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int a;
        cin >> a;
        if (a == 0)
        {
            cout << "CASE #" << i + 1 <<": INSOMNIA" << endl;
        }
        else
        {
            int b = sheep(a);
            cout << "CASE #" << i + 1 << ": " << b << endl;
        }
    }
    return 0;
}
