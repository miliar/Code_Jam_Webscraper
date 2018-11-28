#include <iostream>
#include <algorithm>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string.h>
using namespace::std;

bool possible(string& str)
{
    string s = str;
    while (s.size() > 1)
    {
        string tmp = "";
        for (int i = 0; i < s.size(); i += 2)
        {
            if ((s[i] == 'r' && s[i + 1] == 's') || (s[i] == 's' && s[i + 1] == 'r'))
                tmp.push_back('r');
            else if ((s[i] == 'p' && s[i + 1] == 's') || (s[i] == 's' && s[i + 1] == 'p'))
                tmp.push_back('s');
            else if ((s[i] == 'r' && s[i + 1] == 'p') || (s[i] == 'p' && s[i + 1] == 'r'))
                tmp.push_back('p');
            else return false;
        }

        s = tmp;
    }
    return true;
}

int main ()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t)
    {
        int n, r, p, s;
        cin >> n >> r >> p >> s;

        string out = "";
        for (int i = 0; i < p; ++i) out.push_back('p');
        for (int i = 0; i < r; ++i) out.push_back('r');
        for (int i = 0; i < s; ++i) out.push_back('s');

        do
        {
            if (possible(out)) break;
        }while(std::next_permutation(out.begin(),out.end()));

        if (possible(out))
            cout << "Case #" << t + 1 << ": " << out << endl;
        else
            cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
    }
}
