#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool check(string &s)
{
    for (int i = 0; i < s.size(); i ++)
        if (s[i] == '-')
            return false;
    return true;
}

void flip(string &s, int d)
{
    for (int i = 0; i < d; i ++)
        if (s[i] == '-')
            s[i] = '+';
        else
            s[i] = '-';
    reverse(s.begin(), s.begin()+ d);
}

void dfs(string &s, int &minStep, int depth, int index)
{
    if (check(s))
    {
        if (depth < minStep)
            minStep = depth;
        return;
    }
    if (index < 0)
        return;

    if (s[index] == '-')
    {
        if (s[0] == '-')
        {
            flip(s, index+1);
            dfs(s, minStep, depth+1, index-1);
            flip(s, index+1);
        }
        else
        {
            for (int i = index-1; i >= 0; i --)
            {
                if (s[i] == '+')
                {
                    flip(s, i+1);
                    dfs(s, minStep, depth+1, index);
                    flip(s, i+1);
                    break;
                }
            }
        }
    }
    else
        dfs(s, minStep, depth, index-1);
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t ++)
    {
        cout << "Case #" << t << ": ";
        int k = INT_MAX;
        string s;
        cin >> s;
        dfs(s, k, 0, s.size()-1);
        cout << k << endl;
    }
    return 0;
}
