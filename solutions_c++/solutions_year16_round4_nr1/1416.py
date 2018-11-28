#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <string>
#include <vector>
using namespace std;

int n, r, p, s, kol;

string ans;

string arr[2][3] = {{"PR", "PS", "RS"}, {"RS", "PS", "PR"}};


string check(int shift, int x)
{
    string s = "";
    for(int i = 0; i < kol/2; ++i)
    {
        s += arr[x][(i + shift) % 3];
    }
    return s;
}

void compute(string &s, int &tr, int &tp, int &ts)
{
    tr = tp = ts = 0;
    for(int i = 0; i < kol; ++i)
    {
        if(s[i] == 'R')
            ++tr;
        if(s[i] == 'P')
            ++tp;
        if(s[i] == 'S')
            ++ts;
    }
}

string dfs(int r, int p, int s)
{
    if(r + p + s == 1)
    {
        if(r == 1)
            return "R";
        if(p == 1)
            return "P";
        if(s == 1)
            return "S";
    }
    string s1, s2;
    int m;
    m = max(r, p);
        m = max(m, s);
    if((r+p+s) % 3 == 1)
    {
        if(r == m)
        {
            s1 = dfs(r/2, p/2, s/2 + 1);
            s2 = dfs(r/2, p/2 + 1, s/2);
        }
        if(p == m)
        {
            s1 = dfs(r/2, p/2, s/2 + 1);
            s2 = dfs(r/2 + 1, p/2, s/2);
        }
        if(s == m)
        {
            s1 = dfs(r/2 + 1, p/2, s/2);
            s2 = dfs(r/2, p/2 + 1, s/2);
        }
    }else
    {
        if(r != m)
        {
            s1 = dfs(r/2, p/2, s/2 + 1);
            s2 = dfs(r/2, p/2 + 1, s/2);
        }
        if(p != m)
        {
            s1 = dfs(r/2, p/2, s/2 + 1);
            s2 = dfs(r/2 + 1, p/2, s/2);
        }
        if(s != m)
        {
            s1 = dfs(r/2 + 1, p/2, s/2);
            s2 = dfs(r/2, p/2 + 1, s/2);
        }
    }

    //cout << r << p << s << endl;
    //cout << s1 << ' ' << s2 << endl;

    if(s1 < s2)
        return s1 + s2;
    else
        return s2 + s1;
}

int main()
{
    ifstream f1("A-large.in");
    ofstream f2("A-large.out");
    int T;
    f1 >> T;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        f1 >> n >> r >> p >> s;
        kol = 1 << n;
        if((r != kol/3 && r != kol/3 + 1) || (p != kol/3 && p != kol/3 + 1) || (s != kol/3 && s != kol/3 + 1))
        {
            f2 << "IMPOSSIBLE" << endl;
            continue;
        }

        f2 << dfs(r, p, s) << endl;
        continue;


        int tr, tp, ts;
        string str;

        ans = "W";

        for(int j = 0; j < 2; ++j)
        for(int i = 2; i >= 0; --i)
        {
            str = check(i, j);
            compute(str, tr, tp, ts);
            //cout << tr << ' ' << tp << ' ' << ts << endl << str << endl;
            if(tr == r && tp == p && ts == s)
                ans = min(ans, str);
        }
        if(ans[0] == 'W')
            ans = "IMPOSSIBLE";
        f2 << ans << endl;
    }
    return 0;
}

