#include <bits/stdc++.h>
using namespace std;

int main()
{
    #ifdef O_Amay_Valobase_ni
        freopen("B-large.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
    #endif ///O_Amay_Valobase_ni

    int i, j, k, l, ans, tc, cs = 0;
    string s, s1, s2;

    scanf("%d", &tc);

    while(tc-- and cin >> s)
    {
        ans = 0;
        i = 0;
        while(1)
        {
            s1 = "";
            while(i < s.size() and s[i] == '-') s1 += s[i], i++;
            if(s1.size() > 0) ans++;
            if(i == s.size()) break;
            while(i < s.size() and s[i] == '+') i++;
            if(i == s.size()) break;
            ans++;
        }
        printf("Case #%d: %d\n", ++cs, ans);
    }

    return 0;
}
