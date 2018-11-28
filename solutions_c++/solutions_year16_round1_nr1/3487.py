//Eldar Gaynetdinov
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;

    for(int t = 1; t <= T; t++)
    {
        string s; cin >> s;

        string a(1, s.front());

        for(unsigned i = 1; i < s.length(); i++)
        {
            char c = s[i];

            if(c >= a.front())
                a.insert(begin(a), c);
            else
                a.insert(end(a), c);
        }

        cout << "Case #" << t << ": " << a << endl;
    }

    return 0;
}
