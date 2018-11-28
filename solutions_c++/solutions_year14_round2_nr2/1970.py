#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int t, ans;

////////////////////////////////////////////////////////////
// A
////////////////////////////////////////////////////////////
int main()
{
    cin >> t;
    int a, b, k;
    for (int c = 1; c <= t; c++)
    {
        cin >> a >> b >> k;

        ans = 0;

        if (a > b) std::swap(a, b);

        for (int i = 0; i < a;i++)
        for (int j = 0; j < b; j++)
        {
            int s = i&j;
            if (s < k)
                ans++;
        }
        cout << "Case #" << c << ": " << ans << endl;
    }
    return 0;
}