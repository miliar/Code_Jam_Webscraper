#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
int ra, pa, sa;

void count_all(int n, int win)
{
    if (n == 0)
    {
        if (win == 0)
            ra++;
        else if (win == 1)
            pa++;
        else
            sa++;
    }
    else
    {
        if (win == 0)
            count_all(n - 1, 0), count_all(n - 1, 2);
        else if (win == 1)
            count_all(n - 1, 1), count_all(n - 1, 0);
        else
            count_all(n - 1, 2), count_all(n - 1, 1);
    }
}


string min_gen(int n, int win)
{
    if (n == 0)
    {
        if (win == 0)
            return "R";
        else if (win == 1)
            return "P";
        else
            return "S";
    }
    else
    {
        if (win == 0)
        {
            string a = min_gen(n - 1, 0), b = min_gen(n - 1, 2);
            if (a > b)
                swap(a, b);
            return a + b;
        }
        else if (win == 1)
        {
            string a = min_gen(n - 1, 1), b = min_gen(n - 1, 0);
            if (a > b)
                swap(a, b);
            return a + b;
        }
        else
        {
            string a = min_gen(n - 1, 2), b = min_gen(n - 1, 1);
            if (a > b)
                swap(a, b);
            return a + b;
        }
    }
}



int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    cin >> t;
    for (int _ = 1; _ <= t; ++_)
    {
        cout << "Case #" << _ << ": ";
        int r, p, s, n;
        cin >> n >> r >> p >> s;
        string str = "IMPOSSIBLE";
        ra = 0; pa = 0; sa = 0;
        count_all(n, 0);
        if (ra == r && pa == p && sa == s)
        {
            str = min_gen(n, 0);
        }
        ra = 0; pa = 0; sa = 0;
        count_all(n, 1);
        if (ra == r && pa == p && sa == s)
        {
            string two = min_gen(n, 1);
            if (str == "IMPOSSIBLE" || two < str)
                str = two;
        }
        ra = 0; pa = 0; sa = 0;
        count_all(n, 2);
        if (ra == r && pa == p && sa == s)
        {
            string two = min_gen(n, 2);
            if (str == "IMPOSSIBLE" || two < str)
                str = two;
        }
        cout << str << endl;
    }
}
