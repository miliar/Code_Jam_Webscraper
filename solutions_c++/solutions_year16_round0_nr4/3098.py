#include <iostream>

using namespace std;

void solve()
{
    unsigned int k, c, s;
    cin >> k;
    cin >> c;
    cin >> s;
    for(auto i = 1u; i <= k; i++) {
        cout << " " << i;
    }
}

int main()
{
    unsigned int cases;
    cin >> cases;
    for(auto i = 1u; i <= cases; i++) {
        cout << "Case #" << i << ":";
        solve();
        cout << endl;
    }
    return 0;
}
