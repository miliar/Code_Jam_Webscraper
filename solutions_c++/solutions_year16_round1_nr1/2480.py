#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <limits>
#include <algorithm>
#include <cstring>
using namespace std;


const int maxn = 1005;
bool used[maxn];

string getAns(const string &s)
{
    memset(used, 0, maxn * sizeof(bool));
    string ans;
    int pos = s.length() - 1, cur = pos;

    while (pos >= 0)
    {
        cur = pos;
        for (int i = pos - 1; i >= 0; i--)
        {
            if (s[i] > s[cur])
                cur = i;
        }
        ans += s[cur];
        used[cur] = true;
        pos = cur - 1;
    }

    for (int i = 0; i < (int)s.length(); i++)
        if (!used[i])
            ans += s[i];
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    string s;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> s;
        cout << "Case #" << to_string(i + 1) << ": ";
        cout << getAns(s) << endl;
    }


    fclose(stdin);
    fclose(stdout);
    return 0;
}