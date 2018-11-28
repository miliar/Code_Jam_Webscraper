#include <iostream>

using namespace std;

long solve(int S, string s)
{
    long ans = 0, p = s[0] - '0';

    for(int i = 1; i <= S; ++i) 
    {
        if(i > p && s[i] != '0')
        {
            ans += i - p;
            p += i - p;
        }
        p += s[i] - '0';
    }

    return ans;
}

int main()
{
    //freopen("out.txt", "w", stdout);
    //freopen("in.txt", "r", stdin);

    int T, S;
    cin >> T;
    string s;
    for(int i = 0; i < T; ++i)
    {
        cin >> S >> s;
        cout << "Case #" << (i + 1) << ": " << solve(S, s) << endl;
    }

    return 0;
}
