#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

string sss[1000];
int histogram[1000000];

vector<vector<string> > combo;
int m, n;

int triesize(vector<string> &strs) {
    if (strs.size() == 0) {
        cout << "triesize error! size 0" << endl;
        return 0;
    }
    set<string> sssss;
    for (int i = 0; i < strs.size(); i++) {
        for (int j = 0; j <= strs[i].length(); j++) {
            sssss.insert(strs[i].substr(0, j));
        }
    }
    return sssss.size();
}

void printcombo() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < combo[i].size(); j++) {
            cout << combo[i][j] << " ";
        }
        cout << endl;
    }
}

int dfs(int i) {
    if (i == m) {
        for (int j = 0; j < n; j++) {
            if (combo[j].size() == 0) {
                return 0;
            }
        }
        int res = 0;
        for (int j = 0; j < n; j++) {
            res += triesize(combo[j]);
        }
        histogram[res]++;
        //printcombo(); 
        //cout << res << endl;
        //cout << endl;
        return res;
    }
    int best = 0;
    for (int j = 0; j < n; j++) {
        combo[j].push_back(sss[i]);
        best = max(best, dfs(i+1));
        combo[j].pop_back();
    }
    return best;
}

int main() {
    int ncases;
    cin >> ncases;
    for (int csnum = 1; csnum <= ncases; csnum++) {
        cin >> m >> n;
        for (int i = 0; i < m; i++) {
            cin >> sss[i];
        }
        memset(histogram, 0, sizeof(histogram));
        combo.clear();
        for (int i = 0; i < n; i++) {
            combo.push_back(vector<string>());
        }
        int res = dfs(0);
        cout << "Case #" << csnum << ": " << res << " " << histogram[res] << endl;
    }
}
