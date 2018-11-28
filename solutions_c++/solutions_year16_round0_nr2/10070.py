#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
using namespace std;

int rf(int i, string & s) {
    if (i == -1)
        return 0;
    else if (s[i] == '+')
        return rf(i - 1, s);
    else if (s[0] == '-') {
        reverse(s.begin(), s.begin() + i + 1);
        for (int j = 0; j <= i; ++j)
            s[j] = (s[j] == '+' ? '-' : '+');
        return 1 + rf(i - 1, s);
    }
    else {
        int m = 300;
        for (int j = 0; j < i; ++j) {
                string st = s;
            if (s[j] == '+') {
                reverse(st.begin(), st.begin() + j + 1);
                for (int k = 0; k <= j; ++k)
                    st[k] = (st[k] == '+' ? '-' : '+');
                m = min(m, 1 + rf(i, st));
            }
        }
        return m;
    }
}


int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        string s;
        in >> s;
        out << "Case #" << i + 1 << ": " << rf(s.size() - 1, s) << '\n';
    }
}
