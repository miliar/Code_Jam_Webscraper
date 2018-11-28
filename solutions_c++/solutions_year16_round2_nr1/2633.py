#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct d
{
    char c;
    string str;
    string v;
};

d zero{'Z', "ZERO", "0"};
d one{'O', "ONE", "1"};
d two{'W', "TWO", "2"};
d three{'T', "THREE", "3"};
d four{'U', "FOUR", "4"};
d five{'F', "FIVE", "5"};
d six{'X', "SIX", "6"};
d seven{'S', "SEVEN", "7"};
d eight{'G', "EIGHT", "8"};

// reste nine

vector<d> a = {zero, two, four, six, eight};
vector<d> b = {one, three, five, seven};

void f(string& s, vector<d>& v, string& res)
{
    for (auto& digit : v)
    {
        int here = 0;

        for (char& c : s)
            if (c == digit.c)
                here++;

        for (int i = 0; i < here; i++)
        {
            res += digit.v;

            for (char& c : digit.str)
            {
                for (auto it = s.begin(); it != s.end(); it++)
                {
                    if (*it == c)
                    {
                        s.erase(it);
                        break;
                    }
                }
            }
        }
    }
}

int main()
{
    int n;
    cin >> n;

    for (int t_i = 0; t_i < n; t_i++)
    {
        string s;
        cin >> s;

        string res;

        f(s, a, res);
        f(s, b, res);

        int n_nine = s.size() / 4;

        for (int i = 0; i < n_nine; i++)
            res += "9";

        sort(res.begin(), res.end());

        cout << "Case #" << t_i + 1 << ": ";
        cout << res;
        cout << endl;
    }
}
