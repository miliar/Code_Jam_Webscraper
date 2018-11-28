#include <bits/stdc++.h>
#define lli long long int
#define s(x) scanf("%lld", &x);
lli mod = 1000000007;
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    lli t, n, i, j, ans, l, ta = 1;
    string s;

    s(t);
    while(t--) {
        n = 0;
        s.clear();
        cin>>s;
        l = s.length();
        for (i = l - 1; i >= 0; i--) {
            if (s[i] == '-') {
                n++;
                for (j = i; j >= 0; j--) {
                    if (s[j] == '-') {
                        s[j] = '+';
                    } else {
                        s[j] = '-';
                    }
                }
            }
        }
        cout<<"Case #"<<ta<<": "<<n<<endl;
        ta++;
    }
    return 0;
}
