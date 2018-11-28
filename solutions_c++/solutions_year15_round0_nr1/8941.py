#include <bits/stdc++.h>

#define For(i, be, en) for(i = be; i <= en; i++)
#define Forr(i, be, en) for(int i = be; i >= en; i--)

using namespace std;

int main()
{
    int t, sm, ct, ans;
    string s;
    ofstream out;
    out.open ("D:\\output1.txt");
    ifstream infile("D:\\A-large.in");

    int a[205];

    infile >> t;
    for (int j = 1; j <= t; j++) {
        infile >> sm >> s;

        ct = s[0] - '0';
        ans = 0;
        for (int i = 1; i < sm+1; i++) {
            if (s[i] != 0) {
                if (ct >= i) {
                    ct += s[i] - '0';
                } else {
                    ans += i - ct;
                    ct += i - ct + s[i] - '0';
                }
            }
        }

        a[j] = ans;

    }

    for (int j = 1; j <= t; j++) {
        out <<"Case #" << j << ": " << a[j] << endl;
    }


	return 0;
}
