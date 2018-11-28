#include <vector>
#include<cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <cassert>
#endif
#include <ctime>
#include <queue>
#include <stack>
#include<iomanip>
#include <sstream>
#include <cmath>
using namespace std;
typedef long long ll;
typedef pair<int, int> PII;
const int inf = 0x3fffffff;

int m, n, ans, cnt;
int trie_node(vector<string>& str) {
    sort(str.begin(), str.end());
    int ret = 1;
    for(int i = 0; i < str.size(); i ++) {
        if (i == 0) ret += str[0].size();
        else {
            for(int j = 0; j < str[i].size(); j ++) {
                if (j >= str[i - 1].size() || str[i][j] != str[i - 1][j]) {
                    ret += str[i].size() - j;
                    break;
                }
            }
        }
    }
    return ret;
}
int calc(vector<int>& go, vector<string>& str) {
    int ret = 0;
    for(int i = 0; i < n; i ++) {
        vector<string> tmp;
        for(int j = 0; j < m; j ++) {
            if (go[j] == i) {
                tmp.push_back(str[j]);
            }
        }
        ret += trie_node(tmp);
    }
    return ret;
}
bool check(vector<int>& go) {
    vector<int> cnt(n);
    for(auto i : go) cnt[i] ++;
    for(auto i : cnt) if (i == 0) return false;
    return true;
}
void dfs(int i, vector<int>& go, vector<string>& str) {
    if (i == m) {
        if (!check(go)) return;
        int tmp = calc(go, str);
        if (tmp > ans) {
            ans = tmp;
            cnt = 1;
        } else if (tmp == ans){
            cnt ++;
        }
        return;
    }
    for(int j = 0; j < n; j ++) {
        go[i] = j;
        dfs(i + 1, go, str);
    }
}
void solve(int ncase) {
    cin >> m >> n;
    vector<string> str(m);
    for(int i = 0; i < m; i ++) {
        cin >> str[i];
    }
    vector<int> go(m);
    ans = 0;
    dfs(0, go, str);
    cout << "Case #" << ncase << ": " << ans << " " << cnt << endl;
}

int main() {
    ios::sync_with_stdio(false);
    //cout << setprecision(16) << endl;
#ifdef _zzz_
  freopen("D-small-attempt0.in", "r", stdin);
   freopen("out.txt", "w", stdout);
#endif
    int T = 1;
    cin >> T;
    //scanf("%d", &T);
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
}
