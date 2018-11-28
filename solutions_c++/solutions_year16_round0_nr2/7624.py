#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("ou.txt", "w", stdout);
    int t, cnt;
    string s;
    scanf("%d", &t);
    for(int x = 1; cnt = 0, x <= t; x++){
        cin >> s;
        if(s[0] == '-')cnt++;
        for(int i = 0; i + 1 < s.size(); i++)cnt += 2 * (s[i] == '+' && s[i + 1] == '-');
        printf("Case #%d: %d\n", x, cnt);
    }
    return 0;
}
