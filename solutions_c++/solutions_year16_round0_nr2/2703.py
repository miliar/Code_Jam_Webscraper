#include <iostream>
#include <string>

using namespace::std;

void flip(string& s, int j)
{
    for (int i = 0; i < (j >> 1); ++i)
    {
        char c = s[i];
        s[i] = s[j - i];
        s[j - 1] = c;
    }
}

void normalize(string& s)
{
    string tmp = "";
    for (int i = 0; i < s.size(); ++i)
    {
        if (tmp.size() == 0)
        {
            tmp.push_back(s[i]);
            continue;
        }

        if (s[i] != tmp[tmp.size() - 1])
            tmp.push_back(s[i]);
    }

    s = tmp;
}

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t)
    {
        string s;
        cin >> s;
        normalize(s);

        int ans = 0;
        if (s[0] == '+')
        {
            if (s.size() % 2 == 0) ans = s.size();
            else ans = s.size() - 1;
        }
        else
        {
            if (s.size() % 2 == 0) ans = s.size() - 1;
            else ans = s.size();
        }

        cout << "Case #" << t + 1 << ": " << ans << endl;
    }
}
