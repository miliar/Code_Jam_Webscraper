#include<iostream>
#include<vector>
#include<sstream>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

int solve()
{
    set<string> Eng;
    set<string> French;
    set<string> Both;
    set<string> Unknown;
    string s;
    int n, i;
    int ans = 1000000000;
    cin >> n;
    vector<vector<string> > Words(n);
    getline(cin, s);
    getline(cin, s);
    istringstream sin1(s);
    string word;
    while (sin1 >> word)
        Eng.insert(word); 
    getline(cin, s);
    istringstream sin2(s);
    while (sin2 >> word)
    {
        if (Eng.count(word))
        {
            Eng.erase(word);
            Both.insert(word);
        }
        else
        {
            French.insert(word);
        }
    }
    for (i = 2; i < n; ++i)
    {
        getline(cin, s);
        istringstream sin3(s);
        string word;
        while (sin3 >> word)
        {
            if (!Both.count(word))
            {
                Words[i].push_back(word);
                Unknown.insert(word);
            }
        }
    }
    map <string, int> M_saved;
    for (auto it = Eng.begin(); it != Eng.end(); ++it)
        if (Unknown.count(*it))
            M_saved[*it] = 1;
    for (auto it = French.begin(); it != French.end(); ++it)
        if (Unknown.count(*it))
            M_saved[*it] = 2;
    int mask;
    for (mask = 0; mask < (1 << (n - 2)); ++mask)
    {
        map<string, int> M = M_saved;
        for (int j = 2; j < n; ++j)
        {
            if (mask & (1 << (j - 2)))
            {
                for (i = 0; i < Words[j].size(); ++i)
                    M[Words[j][i]] |= 1;
            }
            else
            {
                for (i = 0; i < Words[j].size(); ++i)
                    M[Words[j][i]] |= 2;
            }
        }
        int curr_ans = 0;
        for (auto it = M.begin(); it != M.end(); ++it)
        {
            if (it -> second == 3)
                curr_ans ++;
        }
        if (curr_ans < ans)
            ans = curr_ans;
    }
    return ans + Both.size();
}

int main()
{
    int T, t;
    cin >> T;
    for (t = 1; t <= T; ++t)
        cout << "Case #" << t << ": " << solve() << endl;
    return 0;
}

