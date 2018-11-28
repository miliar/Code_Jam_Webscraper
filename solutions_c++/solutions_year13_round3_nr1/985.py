#include <iostream>
#include <cstdio>

using namespace std;

string s;
long long a[1100000];

long long cnt(int n)
{
    int last = -1;
    a[0] = 0;
    if (n == 1 && s[0] != 'a' && s[0] != 'e' && s[0] != 'i' && s[0] != 'o' && s[0] != 'u')
    {
        a[0] = 1;
        last = 0;
    }
    int k = s.size();
    int curr = 0;
    if (s[0] == 'a' || s[0] == 'e' || s[0] == 'i' || s[0] == 'o' || s[0] == 'u')
    {
        curr = 0;
    }
    else
    {
        curr++;
    }
    for (int i = 1; i < k; i++)
    {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
        {
            curr = 0;
        }
        else
        {
            curr++;
        }
        if (curr >= n)
        {
            last = i - n + 1;
        }
        a[i] = a[i - 1] + last + 1;
    }
    return a[k - 1];
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int p = 0; p < t; p++)
    {
        int n;
        cin >> s >> n;
        cout << "Case #" << p + 1 << ": ";
        cout << cnt(n) << endl;
    }

    return 0;
}

