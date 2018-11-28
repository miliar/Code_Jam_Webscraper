#include <iostream>
#include <set>

using namespace std;

typedef pair<int, int> p;

void check1(string s[], set<p> &v, int i, int c)
{
    for (int j = 0; j < c; j++)
    {
        if (s[i][j] != '.')
        {
            if (s[i][j] == '<')
            {
                v.insert(p(i, j));
                return;
            }
            else
                return;
        }
    }
}

void check2(string s[], set<p> &v, int i, int c)
{
    for (int j = c - 1; j >= 0; j--)
    {
        if (s[i][j] != '.')
        {
            if (s[i][j] == '>')
            {
                v.insert(p(i, j));
                return;
            }
            else
                return;
        }
    }
}

void check3(string s[], set<p> &v, int j, int r)
{
    for (int i = 0; i < r; i++)
    {
        if (s[i][j] != '.')
        {
            if (s[i][j] == '^')
            {
                v.insert(p(i, j));
                return;
            }
            else
                return;
        }
    }
}

void check4(string s[], set<p> &v, int j, int r)
{
    for (int i = r - 1; i >= 0; i--)
    {
        if (s[i][j] != '.')
        {
            if (s[i][j] == 'v')
            {
                v.insert(p(i, j));
                return;
            }
            else
                return;
        }
    }
}

bool f(string s[], int i, int j, int r, int c)
{
    for (int k = 0; k < r; k++)
    {
        if (s[k][j] != '.' && k != i)
            return true;
    }
    for (int k = 0; k < c; k++)
    {
        if (s[i][k] != '.' && k != j)
            return true;
    }
    return false;
}

int solve()
{
    int r, c;
    cin >> r;
    cin >> c;
    string s[r];
    set<p> v;
    for (int i = 0; i < r; i++)
    {
        cin >> s[i];
    }
    for (int i = 0; i < r; i++)
    {
        check1(s, v, i, c);
        check2(s, v, i, c);
    }
    for (int j = 0; j < c; j++)
    {
        check3(s, v, j, r);
        check4(s, v, j, r);
    }
    for (auto it = v.begin(); it != v.end(); it++)
    {
        if (!f(s, it->first, it->second, r, c))
            return -1;
    }
    return v.size();
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++)
    {
        int s = solve();
        if (s == -1)
           cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i << ": " << s << endl;
    }
    return 0;
}
