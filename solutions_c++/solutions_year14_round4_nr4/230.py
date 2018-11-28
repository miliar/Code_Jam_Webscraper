#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

class AhoCorasick
{
    int n;
    vector<vector<int> > next;
    vector<bitset<64> > match;
    vector<int> failure;
public:
    AhoCorasick(const vector<string>& pattern){
        next.assign(1, vector<int>(128, -1));
        match.assign(1, 0);
        for(unsigned i=0; i<pattern.size(); ++i){
            int curr = 0;
            for(unsigned j=0; j<pattern[i].size(); ++j){
                if(next[curr][pattern[i][j]] == -1){
                    next[curr][pattern[i][j]] = next.size();
                    next.push_back(vector<int>(128, -1));
                    match.push_back(0);
                }
                curr = next[curr][pattern[i][j]];
            }
            match[curr][i] = true;
        }

        n = next.size();
        failure.resize(n, 0);
        vector<int> node1(1, 0);
        while(!node1.empty()){
            vector<int> node2;
            for(unsigned i=0; i<node1.size(); ++i){
                for(int j=0; j<128; ++j){
                    int s = node1[i];
                    if(next[s][j] == -1)
                        continue;
                    node2.push_back(next[s][j]);
                    int t = s;
                    while(t != 0){
                        if(next[failure[t]][j] != -1){
                            failure[next[s][j]] = next[failure[t]][j];
                            match[next[s][j]] |= match[next[failure[t]][j]];
                            break;
                        }
                        t = failure[t];
                    }
                }
            }
            node1.swap(node2);
        }
    }
    int size(){
        return n;
    }
    int transit(int curr, char c){
        if(next[curr][c] != -1)
            return next[curr][c];
        if(curr == 0)
            return 0;
        return transit(failure[curr], c);
    }
    bitset<64> checkMatch(int curr){
        return match[curr];
    }
};

pair<int, int> dfs(int k, vector<string>& s, vector<vector<int> >& group)
{
    if(k == s.size()){
        int ret = 0;
        for(unsigned i=0; i<group.size(); ++i){
            vector<string> t;
            for(unsigned j=0; j<group[i].size(); ++j)
                t.push_back(s[group[i][j]]);

            if(t.size() > 0){
                AhoCorasick ac(t);
                ret += ac.size();
            }
        }
        return make_pair(ret, 1);
    }

    pair<int, int> ret(INT_MIN, 0);
    for(unsigned i=0; i<group.size(); ++i){
        group[i].push_back(k);

        pair<int, int> p = dfs(k+1, s, group);
        if(p.first > ret.first)
            ret = p;
        else if(p.first == ret.first)
            ret.second += p.second;

        group[i].pop_back();
    }
    return ret;
}

pair<int, int> solve()
{
    int m, n;
    cin >> m >> n;
    vector<string> s(m);
    for(int i=0; i<m; ++i)
        cin >> s[i];

    vector<vector<int> > group(n);
    return dfs(0, s, group);
}

int main()
{
    int T;
    cin >> T;

    for(int tc=1; tc<=T; ++tc){
        pair<int, int> ret = solve();
        cout << "Case #" << tc << ": " << ret.first << ' ' << ret.second << endl;
    }

    return 0;
}