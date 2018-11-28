#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        int n;
        cin >> n;

        string s;
        getline(cin, s);
        map<string, int> m;
        vector<vector<int> > v(n);

        for (int i = 0; i < n; i++)
        {
            getline(cin, s);
            stringstream sin(s + " ");

            for (; ; )
            {
                string w;
                sin >> w;

                if (sin.eof())
                    break;

                if (!m.count(w))
                {
                    int x = m.size();
                    m[w] = x + 1;
                }

                v[i].push_back(m[w]);
            }
        }

        int ans = 1 << 30;

        for (int m = 2; m < 1 << n; m += 4)
        {
            int d[1 << 12] = {};

            for (int i = 0; i < n; i++)
                for (int j = 0; j < v[i].size(); j++)
                    d[v[i][j]] |= (m >> i & 1) + 1;

            int cur = 0;
            for (int i = 0; i < 1 << 12; i++)
                cur += d[i] == 3;

            ans = min(ans, cur);
        }

        cout << "Case #" << tt << ": " << ans << endl;
    }

    return 0;
}
