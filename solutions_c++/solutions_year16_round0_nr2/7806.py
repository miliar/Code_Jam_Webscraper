#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int TT;
    cin >> TT;

    for (int T = 1; T <= TT; ++T)
    {
        char s[110];
        int l, ans = 0;
        cin >> s;
        l = strlen(s);
        for (int i = 1; i < l ; ++i)
            ans += (s[i-1] != s[i])?1:0;
        if (s[l-1] == '-')
            ++ans;
        cout << "Case #" << T << ": " << ans << endl;
    }


    fclose(stdin);
    fclose(stdout);
}
