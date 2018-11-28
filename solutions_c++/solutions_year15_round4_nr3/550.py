#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <fstream>
#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <functional>
#include <sstream>

using namespace std;

int main(int argc, char ** argv)
{

    int T;
    while (cin >> T)
    {
        for (int cas = 1; cas <= T; cas ++)
        {
            int n;
            cin >> n;
            string str;
            vector<string> sen(n);
            getline(cin, str);
            vector<vector<int> > a(n);
            vector<vector<int> > edge(n, vector<int>(n, 0));
            map<string, int> name2id;
            string s; 
            for (int i = 0; i<n; i++)
            {
                getline(cin, s);
                istringstream sin(s);
                string str;
                while (sin >> str)
                {
                    if (name2id.count(str) == 0)
                        name2id[str] = name2id.size();
                    a[i].push_back(name2id[str]);
                }
                sort(a[i].begin(), a[i].end());
            }
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                {
                    size_t u = 0, v = 0;
                    while (u < a[i].size() && v < a[j].size())
                    {
                        if (a[i][u] > a[j][v]) 
                            v++;
                        else if (a[i][u] < a[j][v])
                            u++;
                        else 
                            edge[i][j]++, u++, v++;
                    }
                }
                
            vector<int> mk(n);
            int state = 1;
            int ans = 0;
            if (n == 2)
            {
                set<int> e, f;
                state = 1;
                for (int i = 0; i < n; i++)
                {
                    if (state & 1)
                        for (auto &s: a[i]) e.insert(s);
                    else
                        for (auto &s: a[i]) f.insert(s);
                    state >>= 1;
                }
                for (const auto & s: e)
                    ans += f.count(s);
            }else
            {
                ans = 1000000000;
                vector<int> E,F;
                
                for (int to_add = 0; to_add < (1 <<(n - 2)); to_add++)
                {
                    state = to_add;
                    vector<int> e(a[0]),f(a[1]);
                    e.reserve(1000 + 20 * 10);
                    f.reserve(1000 + 20 * 10);
                    for (int i = 2; i < n; i++)
                    {
                        if (state & 1)
                            for (auto &s: a[i]) e.push_back(s);
                        else
                            for (auto &s: a[i]) f.push_back(s);
                        state >>= 1;
                    }
                    sort(e.begin(), e.end());
                    sort(f.begin(), f.end());
                    size_t u = 0, v = 0;
                    int tmp = 0;
                    while (u < e.size() && v < f.size())
                    {
                        if (e[u] > f[v]) 
                            v++;
                        else if (e[u] < f[v])
                            u++;
                        else
                            tmp++, u++, v++;
                        if (tmp >= ans) break;
                    }
                    //clog << "state = "<< to_add <<", tmp = " << tmp << endl;
                    ans = min(ans, tmp);
                }
            }

            clog << "cas =  " << cas << endl; 
            printf("Case #%d: %d\n", cas, ans);

        }
    }
    return 0;
}
