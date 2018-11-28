#include <iostream>
#include <fstream>

#define fs first
#define sc second


using namespace std;

int main()
{
    //int f = 2300;
    //rev(f);
    //cout << f;
    freopen("B-small-attempt2 (2).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cout.precision(40);
    int t;
    cin >> t;
    for (int j = 1; j <= t; ++j)
    {
        int n;
        long double v, x;
        cin >> n >> v >> x;
        pair <long double, long double> s[n];
        for (int i = 0; i < n; ++i)
            cin >> s[i].fs >> s[i].sc; // rate temp
        if (n == 2)
        {
            if (s[0].fs < s[1].fs)
            {
                swap(s[0], s[1]);
            }
            if (s[0].sc == x && s[1].sc == x)
            {
                cout << "Case #" << j << ": " << (long double)v/(s[0].fs + s[1].fs) << endl;
                continue;
            }
            if (s[0].sc == x)
            {
                cout << "Case #" << j << ": " << (long double)v/s[0].fs << endl;
                continue;
            }
            if (s[1].sc == x)
            {
                cout << "Case #" << j << ": " << (long double)v/s[1].fs << endl;
                continue;
            }
            long double k = (s[0].sc - x) / (x - s[1].sc);
            if (k < 0)
            {
                cout << "Case #" << j << ": IMPOSSIBLE" << endl;
            }
            else
            {
                //cerr << k << endl;
                cout << "Case #" << j << ": " << max(v/((1+k) * s[0].fs), k * v / ((1 + k) * s[1].fs)) << endl;
            }

        }
        else
        {
            if (s[0].sc != x)
                cout << "Case #" << j << ": IMPOSSIBLE" << endl;
            else
                cout << "Case #" << j << ": " << v/s[0].fs << endl;
        }
    }
}
