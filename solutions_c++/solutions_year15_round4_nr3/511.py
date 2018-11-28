#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

const int N = 20;

vector<string> all;
vector<string> line[N];
vector<int> ids[N];
int n, answer;
int english[N * 1000], french[N * 1000];

void dfs(int iter) {
    if (iter == n) {
        int cnt = 0;
        for (int i = 0; i < all.size(); ++i) {
            cnt += english[i] && french[i];
        }
        answer = min(answer, cnt);
    } else {
        for (int i = 0; i < ids[iter].size(); ++i) {
            int id = ids[iter][i];
            english[id]++;
        }
        dfs(iter + 1);
        for (int i = 0; i < ids[iter].size(); ++i) {
            int id = ids[iter][i];
            english[id]--;
            french[id]++;
        }
        dfs(iter + 1);
        for (int i = 0; i < ids[iter].size(); ++i) {
            int id = ids[iter][i];
            french[id]--;
        }
    }
}

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tn;
    cin >> tn;
    for (int ti = 1; ti <= tn; ++ti) {
        cin >> n;
        cin.ignore(1);
        all.clear();
        for (int i = 0; i < n; ++i) {
            string buffer;
            getline(cin, buffer);
            stringstream ss(buffer);
            line[i].clear();
            string word;
            while (ss >> word) {
                line[i].push_back(word);
            }
            sort(line[i].begin(), line[i].end());
            line[i].erase(unique(line[i].begin(), line[i].end()), line[i].end());
            all.insert(all.end(), line[i].begin(), line[i].end());
        }
        sort(all.begin(), all.end());
        all.erase(unique(all.begin(), all.end()), all.end());
        
        assert(all.size() < N * 1000);
        
        for (int i = 0; i < n; ++i) {
            ids[i].clear();
            for (int j = 0; j < line[i].size(); ++j) {
                string str = line[i][j];
                
                assert(!str.empty());
                
                int p = lower_bound(all.begin(), all.end(), str) - all.begin();
                ids[i].push_back(p);
            }
            sort(ids[i].begin(), ids[i].end());
            ids[i].erase(unique(ids[i].begin(), ids[i].end()), ids[i].end());
        }
        memset(english, 0, sizeof(english));
        memset(french, 0, sizeof(french));
        for (int i = 0; i < ids[0].size(); ++i) {
            int id = ids[0][i];
            english[id]++;
        }
        for (int i = 0; i < ids[1].size(); ++i) {
            int id = ids[1][i];
            french[id]++;
        }
        answer = 1e9;
        dfs(2);
        cout << "Case #" << ti << ": " << answer << '\n';
    }    
}

