#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

#define foreach(it, s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define X first
#define Y second

const int MAX_N = 100001;
const int MAX_M = 100001;
const int MOD = 1e9 + 7.5;
const double EPS = 1e-8;

int n, m, maxnode, cnt;
vector<string> str;
int p[100];
vector<string> v[32];
set< vector< vector<int> > > answer;
vector<int> pos[10];

void init() {
    str.clear();
    string st;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> st;
        str.push_back(st);
    }
}

int calcnode(vector<string> &v) {
    int ret = v[0].size();
    for (int i = 1; i < v.size(); i++) {
        ret += v[i].size();
        for (int j = 0; j < min(v[i].size(), v[i - 1].size()); j++) {
            if (v[i][j] == v[i - 1][j]) --ret; else break;
        }
    }
    return ret + 1;
}

int calc() {
    int ret = 0;
    for (int i = 0; i < m; i++) {
        sort(v[i].begin(), v[i].end());
        sort(pos[i].begin(), pos[i].end());
        ret += calcnode(v[i]);
    }
    return ret;
}

void dfs(int node, int now) {
    v[node].clear();
    pos[node].clear();
    if (node == m - 1) {
        for (int i = now; i < n; i++) v[node].push_back(str[p[i]]), pos[node].push_back(p[i]);
        int tnode = calc();
        if (tnode > maxnode) {
            maxnode = tnode;
            cnt = 1;
            vector< vector<int> > temp;
            for (int i = 0; i < m; i++) temp.push_back(pos[i]);
            answer.clear();
            answer.insert(temp);
        } else if (tnode == maxnode){
            vector< vector<int> > temp;
            for (int i = 0; i < m; i++) temp.push_back(pos[i]);
            if (answer.find(temp) != answer.end()) return;
            answer.insert(temp);
            ++cnt;
        }
    } else {
        for (int i = now; i < n - 1; i++) {
            v[node].push_back(str[p[i]]);
            pos[node].push_back(p[i]);
            dfs(node + 1, i + 1);
        }
    }
}

void solve(int ca) {
    answer.clear();
    maxnode = 0, cnt = 0;
    for (int i = 0; i < n; i++) p[i] = i;
    do {
        dfs(0, 0);
    } while (next_permutation(p, p + n));
    printf("Case #%d: %d %d\n", ca, maxnode, cnt);
}

int main(){
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    int ca;
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        if(i>=50) break;
        init();
        solve(i + 1);
    }
    return 0;
}
