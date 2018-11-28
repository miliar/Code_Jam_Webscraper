#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int main ()
{
    freopen ("1b.txt", "w", stdout);
    freopen ("A-large (1).in", "r", stdin);
    int q;
    cin >> q;
    for (int i = 1; i <= q; ++i)
    {
        string s1;
        cin >> s1;
        for (int j = 1; j < s1.size(); ++j)
        {
           if (s1[j] >= s1[0])
           {
               for (int k = j - 1; k >= 0; --k)
                    swap(s1[k], s1[k + 1]);
           }
        }
        cout << "Case #" << i << ": " << s1 << endl;
    }
}
