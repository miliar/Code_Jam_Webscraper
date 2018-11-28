#include <iostream>

using namespace std;

string invert(basic_string<char> a)
{
    {
        for (int i = 0; i < a.size(); i++)
            if (a[i] == '+')
                a[i] = '-';
            else
                a[i] = '+';
    }

    return a;
}

int main()
{
    ios_base::sync_with_stdio(0);

    freopen("B-large.in", "r", stdin);
    freopen("ans.txt", "w", stdout);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        string s;
        cin >> s;

        int ans = 0;

        while(int x = s.find_last_of('-') + 1)
        {
            string buf = invert(s.substr(0, x));

            s.erase(s.begin(), s.begin() + x);
            s.insert(0, buf);

            ans++;
        }

        cout << "Case #" << i + 1 << ": " << ans << endl;
    }

    return 0;
}
