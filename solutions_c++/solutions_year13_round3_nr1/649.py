#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define ll long long
#define int long long

using namespace std;

int f(char c)
{
    return (c == 'a' || c == 'o' || c == 'u' || c == 'i' || c == 'e');
}

main()
{
    int T;
    scanf("%lld", & T);

    for (int t = 0; t < T; t++)
    {
        string s;
        int n;
        cin >> s >> n;
        int d[s.size()];

        if (!f(s[0]) && n == 1)
            d[0] = 1;
        else
            d[0] = 0;
        int counter = 1 - f(s[0]);

        for (int i = 1; i < s.size(); i++)
        {
            if (f(s[i]))
            {
                d[i] = d[i - 1];
                counter = 0;
            }
            else if (counter >= n - 1)
            {
                d[i] = i - n + 2;
                counter++;
            }
            else
            {
                d[i] = d[i - 1];
                counter++;
            }
        }
        int res = 0;

        for (int i = 0; i < s.size(); i++)
            res += d[i];
        printf("Case #%lld: %lld\n", t + 1, res);
    }
}
