#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

char maxChar[1024];
string w;

string dfs(int p)
{
    if (p < 0)  return "";

    if (maxChar[p] == w[p])
        return w[p] + dfs(p - 1);
    else
        return dfs(p - 1) + w[p];
}

int main()
{
    freopen("gcj\\A-large.in", "r", stdin);
    freopen("gcj\\A-large.out", "w", stdout);

    int T, cases = 1;

    cin >> T;
    while (T--)
    {
        cin >> w;
        int L = w.length();

        maxChar[0] = w[0];
        for (int i = 1; i < L; ++i)
            maxChar[i] = max(maxChar[i - 1], w[i]);

        cout << "Case #" << cases++ << ": " << dfs(L - 1) << endl;
    }

    return 0;
}