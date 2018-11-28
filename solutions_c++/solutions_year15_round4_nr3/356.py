#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <map>
using namespace std;

int n;
char buf[200000];
vector<vector<int> > sent;
map<string, int> strtoint;
vector<int> truth;
vector<int> engl;
vector<int> fren;
int ans;

int rec(int k, int curans) {
    if (k == n) {
        return curans;
    }
    truth[k] = 0;
    for (int i = 0; i < int(sent[k].size()); ++i) {
        engl[sent[k][i]]++;
        if (engl[sent[k][i]] == 1 && fren[sent[k][i]] != 0) {
            curans++;
        }
    }
    int bestans = rec(k + 1, curans);
    for (int i = 0; i < int(sent[k].size()); ++i) {
        engl[sent[k][i]]--;
        if (engl[sent[k][i]] == 0 && fren[sent[k][i]] != 0) {
            curans--;
        }
    }
    truth[k] = 1;
    for (int i = 0; i < int(sent[k].size()); ++i) {
        fren[sent[k][i]]++;
        if (fren[sent[k][i]] == 1 && engl[sent[k][i]] != 0) {
            curans++;
        }
    }
    bestans = min(bestans, rec(k + 1, curans));
    for (int i = 0; i < int(sent[k].size()); ++i) {
        fren[sent[k][i]]--;
        if (fren[sent[k][i]] == 0 && engl[sent[k][i]] != 0) {
            curans--;
        }
    }
    return bestans;
}

void solve() {
    engl.clear();
    fren.clear();
    sent.clear();
    truth.clear();
    engl.clear();
    fren.clear();
    
    scanf("%d\n", &n);
    for (int i = 0; i < n; ++i) {
        sent.push_back(vector<int>());
        gets(buf);
        stringstream ss(buf);
        string s;
        while (ss >> s) {
            if (strtoint.count(s) == 0) {
                int tmp = strtoint.size();
                strtoint[s] = tmp;
            }
            sent.back().push_back(strtoint[s]);
        }
    }
    
    truth.resize(n);
    engl.resize(strtoint.size());
    fren.resize(strtoint.size());
    
    for (int i = 0; i < int(sent[0].size()); ++i) {
        engl[sent[0][i]] = 1;
    }

    for (int i = 0; i < int(sent[1].size()); ++i) {
        fren[sent[1][i]] = 1;
    }
    
    ans = 0;
    for (int i = 0; i < int(strtoint.size()); ++i) {
        ans += (engl[i] == 1 && fren[i] == 1);
    }
    
    ans = rec(2, ans);
    
    cout << ans;
}

int main() {
    int t;
    scanf("%d\n", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}
