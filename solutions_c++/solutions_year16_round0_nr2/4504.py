#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        printf("Case #%d: ", i);

        string s;
        cin >> s;

        int k = 0;
        for (int j = s.length() - 1; j >= 0; j--)
        {
            int x = (s[j] == '-') + k;
            if (x % 2 == 1) k++;
        }

        printf("%d\n", k);
    }
}
