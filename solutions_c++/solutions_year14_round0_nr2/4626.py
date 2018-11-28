#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>

using namespace std;

long double c, f, x;

void go()
{
    int cur;
    if (c >= x)
    {
        cout << x/2.0 << endl;
        return;
    }
    long double time = 0;
    long double c_per_sec = 2.0;
    time = c/c_per_sec;
    while (((x - c)/c_per_sec) > ((x - c)/(c_per_sec + f) + c/(c_per_sec + f)))
    {
        c_per_sec += f;
        time += c/c_per_sec;
       // cout << "c_per_sec = "  << c_per_sec << endl;
    }
    time += (x - c)/c_per_sec;
    cout << time << endl;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int t;
    cout.precision(20);
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> c >> f >> x;
       // cout << "File " << c << " " << f << " " << x << endl;
        cout << "Case #" << i + 1 << ": ";
        go();
    }

    return 0;
}
