#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n;
        string s;
        cin >> n >> s;
        int rez = 0, sum = 0;
        sum = int(s[0] - '0');
        for (int j = 1; j < s.length(); ++j)
            if (j <= sum)
                sum += int(s[j] - '0');
            else
            {
                rez += j - sum;
                sum += j - sum + int(s[j] - '0');
            }
        cout << "Case #" << i + 1 << ": " << rez << '\n';
    }
    return 0;
}
