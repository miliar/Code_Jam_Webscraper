#include <bits/stdc++.h>

using namespace std;

int main()
{
    FILE *fi = fopen("A-large.in", "r");
    FILE *fo = fopen("op.txt", "w");

    int t;

    fscanf(fi, "%d", &t);

    for (int lol = 1; lol <= t; lol++) {
        int n, i, j, ans, val;

        char s[1500];

        fscanf(fi, "%d %s", &n, &s);

        //cout << n << " " << s << endl;

        val = 0;
        ans = 0;
        for (i = 0; i <= n; i++) {
            if (val < i) {
                ans += (i - val);

                //cout << "hi " << i << " " << val << endl;

                val = i;
            }

            val += (s[i] - '0');
        }

        //cout << ans << endl;
        fprintf(fo, "Case #%d: %d\n", lol, ans);
    }

    return 0;
}
