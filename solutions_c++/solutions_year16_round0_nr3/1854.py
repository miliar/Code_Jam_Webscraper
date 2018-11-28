#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

string cur;
int n, j;
vector <string> answer;

void recursion(int i)
{
    if (answer.size() == j)
        return;
    if (i > n)
        return;
    if (i > 0 && cur[0] != 1)
        return;
    if (i == n && cur[n - 1] == 1)
    {
        answer.push_back(cur);
        return;
    }
    if (cur[i] == 1)
        recursion(i + 1);
    else
    {
        if (i < n - 1)
            cur[i] = 1,
            cur[i + 1] = 1,
            recursion(i + 2);
        cur[i] = 0;
        cur[i + 1] = 0;
        recursion(i + 1);
    }

}

int main()
{
    freopen("a.out", "w", stdout);
    cout << "Case #1:\n";
    int t;
    cin >> t;
    cin >> n >> j;
    cur = string(n, 0);
    recursion(0);
    for (auto &x : answer)
        for (auto &y : x)
            y+='0';
    for (auto x : answer)
    {
        cout << x << " ";
        for (int i = 2; i <= 10; ++i)
            cout << i + 1 << " ";
        cout << "\n";
    }

    return 0;
}
