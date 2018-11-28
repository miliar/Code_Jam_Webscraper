#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <deque>
using namespace std;

deque <char> a;

int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        string s;
        cin >> s;
        string ans;
        int l = s.length();
        a.clear();
        for (int j = 0; j < l; j++)
        {
            if (j == 0)
            {
                a.push_front(s[j]);
            }
            else
            {
                if (s[j] < a.front())
                {
                    a.push_back(s[j]);
                }
                else
                {
                    a.push_front(s[j]);
                }
            }
        }
        cout << "Case #" << i + 1 << ": ";
        for (int j = 0; j < l; j++)
        {
            cout << a[j];
        }
        cout << endl;
    }
    return 0;
}
