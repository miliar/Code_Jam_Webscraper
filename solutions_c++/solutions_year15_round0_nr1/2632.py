#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int cnt, i, j, n_friend, n_stand, res, s_max, sum, t;
    string temp;
    vector <bool> s1;
    vector <int> s;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> s_max; cin >> temp;
        s.resize(s_max + 1); s1.resize(s_max + 1);
        for (i = 0; i <= s_max; i++) s[i] = temp[i] - '0';

        //for (i = 0; i <= s_max; i++) cout << s[i] << " ";
        //cout << endl; res = s_max;

        sum = 0;
        for (i = 0; i <= s_max; i++) { sum += s[i]; s1[i] = false; }
        n_friend = 0;
        while (true) {
            n_stand = n_friend;
            for (i = 0; i <= s_max; i++) {
                if (n_stand >= i) n_stand += s[i];
            }
            if (n_stand == sum + n_friend) { res = n_friend; break; }
            n_friend++;
        }

        //display results
        cout << "Case #" << cnt << ": " << res << endl;
    }
    return 0;
}
