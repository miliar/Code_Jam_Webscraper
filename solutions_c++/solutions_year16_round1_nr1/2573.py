#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ll long long int
#define s(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define sd(x) scanf("%lf", &x)
#define mod 1000000007
#define get getchar_unlocked

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("CJ1L.txt", "w", stdout);
    int t, i, u = 0;
    string s, h;
    cin >> t;
    while (t--) {
        cin >> s;
        h = "";
        for (i = 0; i < s.size(); ++i) {
            if (s[i]+h <= h+s[i])
                h = h+s[i];
            else
                h = s[i]+h;
        }
        printf("Case #%d: ", ++u);
        cout << h << endl;
    }
    return 0;
}
