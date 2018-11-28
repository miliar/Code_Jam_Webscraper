#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<unsigned short> digits;

unsigned int find_this(string &s, const string &t)
{
    string::size_type p = string::npos;
    unsigned int count = 0;
    while ((p = s.find(t[0])) != string::npos)
    {
        for (char c : t)
            s.erase(s.find(c), 1);
        ++count;
    }
    return count;
}

void add_n_times(unsigned short d, unsigned int n)
{
    for (unsigned int i = 0; i < n; ++i)
        digits.push_back(d);
}

int main()
{
    unsigned short T = 0;
    cin >> T;
    for (unsigned short t = 1; t <= T; ++t)
    {
        string s;
        cin >> s;

        digits.clear();

        unsigned int n = find_this(s, "ZERO");
        add_n_times(0, n);

        n = find_this(s, "WTO");
        add_n_times(2, n);

        n = find_this(s, "UFOR");
        add_n_times(4, n);

        n = find_this(s, "XSI");
        add_n_times(6, n);

        n = find_this(s, "ONE");
        add_n_times(1, n);

        n = find_this(s, "RTHEE");
        add_n_times(3, n);

        n = find_this(s, "TEIGH");
        add_n_times(8, n);

        n = find_this(s, "FIVE");
        add_n_times(5, n);

        n = find_this(s, "VSEEN");
        add_n_times(7, n);

        n = find_this(s, "INNE");
        add_n_times(9, n);

        sort(digits.begin(), digits.end());
        cout << "case #" << t << ": ";
        for (auto it = digits.cbegin(); it != digits.cend(); ++it)
            cout << *it;
        cout << '\n';
    }
}
