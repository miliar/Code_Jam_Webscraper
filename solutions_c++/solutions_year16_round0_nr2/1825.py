#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int q = 1;
    string s;
    ifstream cin("B-large.in");
    ofstream cout("output");
    cin >> q;
    for (int i = 0; i < q; ++i)
    {
        cin >> s;
        s += '+';
        cout << "Case #" << i + 1 << ": " << --unique(s.begin(), s.end()) - s.begin() << '\n';
    }
    return 0;
}
