#include <cstdio>
#include <string>
#include <iostream>
#include <cstdlib>
using namespace std;

int t;
string s;

char rev(char x)
{
    if (x == '+') return '-';
    else        return '+';
}

int find(int x, char goal)
{
    if (x == 0) {
        if (s[x] == goal) return 0;
        else        return 1;
    }
    if (s[x] == goal) return find(x - 1, goal);
    else                return find(x - 1, rev(goal)) + 1;
}

void work()
{
    cin >> t;
    for (int l = 0; l < t; ++l)
    {
        cin >> s;
        int ans = find(s.length() - 1, '+');
        cout << "Case #" << l + 1 << ": " << ans << endl;
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    work();
    return 0;
}
