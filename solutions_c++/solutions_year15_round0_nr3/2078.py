#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <cstdio>
#include <memory>
#include <cstdlib>
#include <cmath>
#include <ctime>

using namespace std;

const int INF = 2147483647;

int M[4][4] = {
    {0, 1, 2, 3},
    {1, 0, 3, 2},
    {2, 3, 0, 1},
    {3, 2, 1, 0}};

int S[4][4] = {
    {1, 1, 1, 1},
    {1, -1, 1, -1},
    {1, -1, -1, 1},
    {1, 1, -1, -1}};

map<char, int> ind = { {'i', 1}, {'j', 2}, {'k', 3} };

int main(int argc, const char * argv[]) {
    srand((unsigned) time(0));
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        int x, l;
        cin >> l >> x;
        string s, s1;
        cin >> s1;
        for(int i = 0; i < x; ++i)
            s += s1;
        bool can = false;
        int cur = 0;
        int cursign = 1;
        set<int> first, last;
        for(int i = 0; i < s.size() - 2; ++i)
        {
            cursign *= S[cur][ind[s[i]]];
            cur = M[cur][ind[s[i]]];
            if(cur == 1 && cursign == 1)
                first.insert(i);
        }
        
        cur = 0;
        cursign = 1;
        
        for(int i = 1; i < s.size() - 1 ; ++i)
        {
            cursign *= S[ind[s[s.size() - i]]][cur];
            cur = M[ind[s[s.size() - i]]][cur];
            if(cur == 3 && cursign == 1)
                last.insert(i);
        }
        
        
        for(auto i : first)
        {
            cursign = 1;
            cur = 0;
            for(int j = i + 1; j < s.size() - 1; ++j)
            {
                cursign *= S[cur][ind[s[j]]];
                cur = M[cur][ind[s[j]]];
                if(cur == 2 && cursign == 1 && last.count((int)s.size() - j - 1) > 0)
                {
                    can = true;
                    break;
                }
            }
            if(can)
                break;
        }

        cout << "Case #" << t << ": " << (can ? "YES" : "NO") << endl;
    }
    
    return 0;
}
