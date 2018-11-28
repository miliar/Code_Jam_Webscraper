#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;

ifstream in("d_small.in");
ofstream out("d_small.out");

int n, m;

int answer1, answer2;

int work(const vector<string>& s)
{
    unordered_set <string> st;
    st.insert("");
    if (s.size() == 0)
        return 0;
    for (int i = 0; i < s.size(); ++i)
    {
        string y;
        for (int j = 0; j < s[i].size(); ++j)
        {
            y = y + s[i][j];
            st.insert(y);
        }
    }
    return st.size();
}

void solve(const vector<string>& s, vector <int> v)
{
    if (v.size() == n)
    {
        vector <string> g[9];
        for (int i = 0; i < n; ++i)
        {            
            g[v[i]].push_back(s[i]);
        }
        int ans = 0;
        for (int i = 0; i < m; ++i)
            ans += work(g[i]);
        if (answer1 == -1 || ans > answer1)
        {
            answer1 = ans;
            answer2 = 1;
        }
        else
        {
            if (ans == answer1)
            {
                /*if (ans == 7)
                {
                    for (int i = 0; i < n; ++i)
                        cout << v[i] << " ";
                    cout << endl;
                }*/
                answer2++;
            }
        }
        return;
    }

    for (int i = 0; i < m; ++i)
    {
        v.push_back(i);
        solve(s, v);
        v.pop_back();
    }

}

int main()
{
    int number;
    in >> number;
    for (int t = 1; t <= number; ++t)
    {        
        in >> n >> m;
        vector <string> s(n);
        for (int i = 0; i < n; ++i)
            in >> s[i];

        vector <int> v;
        answer1 = -1;
        answer2 = -1;
        solve(s, v);
        
        out << "Case #" << t << ": " << answer1 << " " << answer2 << endl;
    }
    return 0;
}