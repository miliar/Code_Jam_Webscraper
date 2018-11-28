#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

bool has_arrow_in_direction(int r, int c, const vector<string>& vec, char a, int i, int j)
{
    if (a == '^')
    {
        for (int k = i - 1; k >= 0; k--)
            if (vec[k][j] != '.')
                return true;
    }
    else if (a == '>')
    {
        for (int k = j + 1; k < c; k++)
            if (vec[i][k] != '.')
                return true;
    }
    else if (a == '<')
    {
        for (int k = j - 1; k >= 0; k--)
            if (vec[i][k] != '.')
                return true;
    }
    else
    {
        for (int k = i + 1; k < r; k++)
            if (vec[k][j] != '.')
                return true;
    }
    return false;
}

inline bool has_chance_to_get_good(int r, int c, const vector<string>& vec, int i, int j)
{
    return has_arrow_in_direction(r, c, vec, '^', i, j) || 
           has_arrow_in_direction(r, c, vec, '>', i, j) ||
           has_arrow_in_direction(r, c, vec, '<', i, j) || 
           has_arrow_in_direction(r, c, vec, 'v', i, j);
}

int solve()
{
    int r, c;
    cin >> r >> c;
    vector<string> vec(r);
    for (int i = 0; i < r; i++)
        cin >> vec[i];
    int ans = 0;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            if (vec[i][j] != '.')
            {
                if (!has_arrow_in_direction(r, c, vec, vec[i][j], i, j))
                {
                    if (has_chance_to_get_good(r, c, vec, i, j))
                        ans += 1;
                    else
                        return -1;
                }
            }
    return ans;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int nans = solve();
        if (nans == -1)
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i + 1 << ": " << nans << endl;
    }
    return 0;
}
