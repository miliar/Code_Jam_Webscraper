#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <sstream>

using namespace std;

int solve()
{
    vector<vector<int> > sentences;
    int n;
    cin >> n;
    sentences.resize(n);
    string s;
    getline(cin, s);
    map<string, int> mp;
    int k = 0;
    for (int i = 0; i < n; i++)
    {
        stringstream ss;
        getline(cin, s);   
        ss << s;
        while (!ss.eof())
        {
            ss >> s;
            if (!mp.count(s))
            {
                mp[s] = k;
                k++;
            }
            sentences[i].push_back(mp[s]);
        }
    }
    int res = 1791791791;
    for (int _mask = 0; _mask < (1 << (n - 2)); _mask++)
    {
        int mask = (_mask << 2) | 1;
//        set<int> eng;
//        set<int> fr;
        vector<bool> eng(k, false);
        vector<bool> fr(k, false);
        for (int i = 0; i < n; i++)
        {
            if ((mask >> i) & 1)
            {
                for (int str : sentences[i])
                    eng[str] = true;
            }
            else
            {
                for (int str : sentences[i])
                {
//                    cout << str << endl;
                    fr[str] = true;
                }
            }
        }
        int ans = 0;
        for (int str = 0; str < k; str++)
        {
            if (fr[str] && eng[str])
                ans += 1;
        }
        res = min(res, ans);
    }
    return res;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
        cout << "Case #" << i << ": " << solve() << endl;
    return 0;
}
