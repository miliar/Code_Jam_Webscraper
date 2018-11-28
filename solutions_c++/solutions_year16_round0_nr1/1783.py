#include <fstream>
#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<int, int> ans;

int main()
{
    int q = 1;
    ifstream cin("A-large.in");
    ofstream cout("output");
    cin >> q;
    for (int i = 0, n, met = 0, j; i < q; ++i, met = 0)
    {
        cin >> n;
        if (!ans.count(n))
            for (int k = (j = n, 0); k < 1000 && met != (1 << 10) - 1; ++k, j += n)
                for (int k = j; k || k == j; k /= 10)
                {
                    met |= 1 << k % 10;
                    if (k == 0)
                        break;
                }
        else
            if (ans[n] > -1)
                met = (1 << 10) - 1, j = ans[n];
        cout << "Case #" << i + 1 << ": ";
        if (met == (1 << 10) - 1)
            cout << (ans[n] = j) - n << '\n';
        else
            cout << "INSOMNIA\n", ans[n] = -1;
    }
    return 0;
}
