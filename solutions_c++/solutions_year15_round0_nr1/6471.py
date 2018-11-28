#include <bits/stdc++.h>
using namespace std;

int main()
{   
    int TC, n, actual, needed, k = 1;
    string s;

    cin >> TC;

    while(TC--)
    {
        actual = 0;
        needed = 0;

        cin >> n >> s;

        for (int i = 0; i < n + 1; ++i)
        {
            if ((i > actual) && (s[i] - '0' > 0)) //more peope needed due to shyness
            {
                needed += i - actual;
                actual += i - actual;
            }
            
            actual += s[i] - '0';
        }

        cout << "Case #" << k++ << ": " << needed << endl;
    }

    return 0;
}
