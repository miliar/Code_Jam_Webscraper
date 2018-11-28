#include <iostream>
#include <cstring>
#include <algorithm>
#include <list>
#include <vector>
#include <string>
using namespace std;

int main() {
    int ntc;
    cin>>ntc;
    for (int tc=1; tc<=ntc; ++tc) {
        string s;
        cin>>s;
        vector<bool> start(s.length());
        for (int i=0; i<start.size(); ++i)
            start[i]=(s[i]=='+'?1:0);
        vector<bool>::iterator iter=unique(start.begin(), start.end());
        start.resize(std::distance(start.begin(), iter));
        vector<bool> finish(start.size(), 1);

        list<pair<vector<bool>, int>> q;
        vector<vector<bool>> intree;
        q.push_back(make_pair(start, 0));
        intree.push_back(start);
        int res=0;
        while (!q.empty()) {
            pair<vector<bool>, int> v=q.front(); q.pop_front();
            finish.resize(v.first.size(), 1);
            if (v.first==finish) {
                res=v.second;
                break;
            }
            for (int i=0; i<v.first.size(); ++i) {
                vector<bool> t=v.first;
                for (int j=i, k=0; j>=0; --j, ++k)
                    t[k]=(v.first[j]==0?1:0);
                vector<bool>::iterator iter=unique(t.begin(), t.end());
                t.resize(std::distance(t.begin(), iter));
                if (find(intree.begin(), intree.end(), t)==intree.end()) {
                    q.push_back(make_pair(t, v.second+1));
                    intree.push_back(t);
                }
            }
        }
        cout<<"Case #"<<tc<<": "<<res<<'\n';
    }
    return 0;
}