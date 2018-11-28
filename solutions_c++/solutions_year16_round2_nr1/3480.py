#include <bits/stdc++.h>

using namespace std;

array<string, 10> mapping{"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool my_is_empty(map<char, int>& occ)
{
    for(char i = 'A'; i <= 'Z'; i++)
    {
        if(occ[i] > 0)
            return false;
    }
    return true;
}

bool is_ok(map<char, int>& occ, int num)
{
    for(int i = 0; i < (int)mapping[num].size(); i++)
    {
        if(occ[mapping[num][i]] <= 0)
        {
            for(int j = 0; j < i; j++)
            {
                occ[mapping[num][j]]++;
            }
            return false;
        }
        occ[mapping[num][i]]--;
    }
    return true;
}

bool try_map(map<char, int>& occ, vector<int>& sol)
{
    if(my_is_empty(occ))
        return true;
    for(int i = 0; i < 10; i++)
    {
        if(is_ok(occ, i))
        {
            //cerr << i << "is ok" << endl;
            sol.push_back(i);
            bool ret = try_map(occ, sol);
            if(ret)
                return true;
            for(int j = 0; j < (int)mapping[i].size(); j++)
            {
                occ[mapping[i][j]]++;
            }
            sol.pop_back();
            //cerr << i << "is not ok" << endl;
        }
    }
    return false;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    for(int caso = 1; caso <= t; caso++)
    {
        //cerr << caso << endl;
        string s;
        cin >> s;
        map<char, int> occ;
        vector<int> sol;
        for(char c: s)
        {
            occ[c]++;
        }
        assert(try_map(occ, sol));
        sort(sol.begin(), sol.end());
        cout << "Case #" << caso << ": ";
        for(auto& i: sol)
            cout << i;
        cout << endl;
    }
    return 0;
}
