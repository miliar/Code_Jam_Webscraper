#include<bits/stdc++.h>
#define all(a) a.begin(), a.end()
#define int long long
int inf = 1e12;
using namespace std;

template <typename T> int sgn(T val)
{
    return (T(0) < val) - (val < T(0));
}

signed main(int argc, char *argv[])
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(0);
    int rules[5][5];
    rules[1][1] = 1;
    rules[1][2] = 2;
    rules[1][3] = 3;
    rules[1][4] = 4;
    rules[2][1] = 2;
    rules[2][2] = -1;
    rules[2][3] = 4;
    rules[2][4] = -3;
    rules[3][1] = 3;
    rules[3][2] = -4;
    rules[3][3] = -1;
    rules[3][4] = 2;
    rules[4][1] = 4;
    rules[4][2] = 3;
    rules[4][3] = -2;
    rules[4][4] = -1;

    int T;
    cin >> T;
    for(int q = 1; q <= T; q++)
    {
        int X, L;
        cin >> X >> L;
        string s;
        cin >> s;
        string ss(s.size(), 'a');
        for(int i = 0; i < s.size(); i++)
            if(s[i] == '1')
                ss[i] = '1';
            else if(s[i] == 'i')
                ss[i] = '2';
            else if(s[i] == 'j')
                ss[i] = '3';
            else
                ss[i] = '4';
        string res = ss;
        for(int i = 0; i < L - 1; i++)
            res += ss;
        int n = X * L;
        if(n < 3)
        {
            cout << "Case #" << q << ": " << "NO" << '\n';;
            continue;
        }
        vector<int> pref(n), suff(n);
        pref[0] = res[0] - '0';
        suff[n - 1] = res[n - 1] - '0';
        for(int i = 1; i < n; i++)
            pref[i] = sgn(pref[i - 1])*rules[abs(pref[i - 1])][res[i] - '0'];

        for(int i = n - 2; i >= 0; i--)
            suff[i] = sgn(suff[i + 1])*rules[res[i] - '0'][abs(suff[i + 1])];

        for(int j = 0; j < n - 2; j++)
        {
            if(pref[j] != 2)
                continue;
            int result = res[j + 1] - '0';
            if(pref[j] == 2 && result == 3 && suff[j + 2] == 4)
            {
                cout << "Case #" << q << ": " << "YES" << '\n';
                goto h;
            }
            for(int k = j + 3; k < n - 1; k++)
            {
                result = sgn(result) * rules[abs(result)][res[k - 1] - '0'];
                if(pref[j] == 2 && result == 3 && suff[k] == 4)
                {
                    cout << "Case #" << q << ": " << "YES" << '\n';
                    goto h;
                }
            }
        }
        cout << "Case #" << q << ": " << "NO" << '\n';
h:
        ;
    }
    return 0;
}
