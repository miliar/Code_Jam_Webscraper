#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int main()
{
    int n, t, i, j;
    set<int> s;
    ifstream cin("A-large.in");
    ofstream cout("output.txt");
    cin >> t;
    for (i = 1; i <= t; i++)
    {
        cin >> n;
        s.clear();
        cout << "Case #" << i << ": ";
        if (n > 0) {
            for (j = n; j > 0; j += n)
            {
                int p = j;
                while (p > 0)
                {
                    s.insert(p % 10);
                    p /= 10;
                }
                if (int(s.size()) == 10)
                {
                    cout << j;
                    break;
                }
            }
        } else
        {
            cout << "INSOMNIA";
        }
        cout << "\n";
    }
    return 0;
}
