#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <cassert>

using namespace std;

string multaux(map< char, map<char, string> >& table, const string& a, const string& b)
{
    if (a.length() == 1 && b.length() == 1)
    {
        return table[a[0]][b[0]];
    }
    else if (a.length() > 1 && b.length() > 1)
    {
        return table[a[1]][b[1]];
    }
    else if (a.length() == 1 && b.length() > 1)
    {
        string res = table[a[0]][b[1]];
        if (res.length() == 1)
            return "-" + res;
        else
            return string(1, res[1]);
    }
    else if (a.length() > 1 && b.length() == 1)
    {
        string res = table[a[1]][b[0]];
        if (res.length() == 1)
            return "-" + res;
        else
            return string(1, res[1]);
    }

    assert(false);
}

string mult(map< char, map<char, string> >& table, vector< vector<string> >& cache, const string& s, int d, int h)
{
    if (d == h)
        return cache[d][h] = s[d];

    if (cache[d][h] != "")
        return cache[d][h];

    int mid = d + ((h - d) / 2);
    return cache[d][h] = multaux(table, mult(table, cache, s, d, mid), mult(table, cache, s, mid + 1, h));
}

bool IsPossible(map< char, map<char, string> >& table, const string& s)
{
    vector< vector<string> > cache (s.length());
    for(int j = 0; j < s.length(); ++j)
        cache[j].resize(s.length());

    for (int i = 0; i < s.length(); ++i)
    {
        if (mult(table, cache, s, 0, i) == "i")
        {
            for (int j = i + 1; j < s.length()-1; ++j)
            {
                if (mult(table, cache, s, i+1, j) == "j" &&
                    mult(table, cache, s, j+1, s.length()-1) == "k")
                    return true;
            }
        }
    }

    return false;
}

int main()
{
    map< char, map<char, string> > table;
    table['1']['1'] = "1";
    table['1']['i'] = "i";
    table['1']['j'] = "j";
    table['1']['k'] = "k";

    table['i']['1'] = "i";
    table['i']['i'] = "-1";
    table['i']['j'] = "k";
    table['i']['k'] = "-j";

    table['j']['1'] = "j";
    table['j']['i'] = "-k";
    table['j']['j'] = "-1";
    table['j']['k'] = "i";

    table['k']['1'] = "k";
    table['k']['i'] = "j";
    table['k']['j'] = "-i";
    table['k']['k'] = "-1";

    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int x;
        cin >> x >> x;

        string text, tmp;
        cin >> tmp;

        for(int j = 0; j < x; ++j)
            text.append(tmp);

        bool possible = tmp.length() > 1 && text.length() >= 3 && IsPossible(table, text);


        cout << "Case #" << i + 1 << ": " << (possible ? "YES" : "NO") << endl;
    }

    return 0;
}
