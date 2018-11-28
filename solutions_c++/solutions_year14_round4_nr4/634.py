#include <iostream>
#include <cmath>
#include <vector>
#include <set>
using namespace std;

string s[8];
vector<string> ts[4];

int main()
{
    int t; cin >> t;
    for (int T = 1; T <= t; T++)
    {
        int m, n;
        cin >> m >> n;
        for (int i = 0; i < m; i++)
            cin >> s[i];
        int x = 0, y = 0;
        // n^m possibilities
        for (int i = 0; i < pow(n,m); i++)
        {
            for (int j = 0; j < n; j++)
                ts[j].clear();
            for (int j = 0; j < m; j++)
            {
                int xx = (i/(int)pow(n,j))%n;
                //cout << xx << " ";
                // j goes in x
                ts[xx].push_back(s[j]);
            }
            //cout << endl;
            int xx = 0;
            for (int j = 0; j < n; j++)
            {
                if (!ts[j].size())
                    continue;
                set<string> ss;
                for (int k = 0; k < ts[j].size(); k++)
                {
                    string cur = "";
                    for (int l = 0; l < ts[j][k].size(); l++)
                    {
                        cur.push_back(ts[j][k][l]);
                        ss.insert(cur);
                    }
                }
                xx += ss.size()+1;
            }
            //cout << xx << endl;
            if (x < xx)
            {
                x = xx;
                y = 1;
            }
            else if (x == xx)
                y++;
            //cout << endl;
        }
        cout << "Case #" << T << ": " << x << " " << y << "\n";
    }
    return 0;
}