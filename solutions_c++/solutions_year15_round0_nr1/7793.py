#include <bits/stdc++.h>
using namespace std;

int main ()
{
    int n;
    cin >> n;
    for (int cases = 0; cases < n; cases++) {
        int smax;
        cin >> smax;

        string str;
        cin >> str;
        vector<int> v(smax + 1);
        for (int i = 0; i < str.size(); i++) {
            v[i] = str[i] - '0';
        }

        int res = 0;
        for (int i = 1; i < v.size(); i++) {
            if (v[i-1] >= i) {
                v[i] += v[i-1];
            } else {
                int sub = i - v[i-1];
                res += sub;
                v[i] += i;
            }
        }

        cout << "Case #" << cases+1 << ": "<< res << endl;
    }

    return 0;
}
