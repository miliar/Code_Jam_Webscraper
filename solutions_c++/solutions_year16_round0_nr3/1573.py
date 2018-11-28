#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

int run(string s)
{

    int q = 1;
    ifstream cin(s + ".in");
    ofstream cout(s + ".out");
    int n, j;
    cin >> n >> n >> j;
    cout << "Case #" << 1 << ":\n";
    for (int msk = (1 << n / 2 - 1) + 1; msk < (1 << n / 2) && j; msk += 2, --j)
    {
        for (int t = msk; t; t >>= 1)
            cout << t % 2;
        for (int t = msk; t; t >>= 1)
            cout << t % 2;
        for (int base = 2; base < 11; ++base)
            cout << ' ' << int64_t(__builtin_roundl(__builtin_powl(base, n / 2))) + 1;
        cout << '\n';
    }
    if (j)
        cerr << s << ": smth bad\n";
}

int main()
{
    run("C-small");
    run("C-large");
    return 0;
}
