#include <cstdio>
#include <cstring>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <functional>
#include <utility>
#include <string>
#include <sstream>
#include <sstream>
using namespace std;
typedef long long ll;
int  s1[100000010], s2[100001000];

const ll B = 29;
const ll P = 99999989;
ll hs(string s) {
    ll res = 0;
    for (auto ch: s) {
        res = (res * B + ch) % P;
    }
    return res;
}
int n;
vector<ll> st[110];
set<ll> sts;

int ans;

void dfs(int cur) {
    if (cur == n) {
        int tmp = 0;
        for (auto i: sts) {
            if (s1[i] > 0 && s2[i] > 0) tmp++;
        }
        ans = min(tmp, ans);
    }
    else {
        for (int i = 0; i < st[cur].size(); i++) {
            s1[st[cur][i]]++;
        }
        dfs(cur+1);
        for (int i = 0; i < st[cur].size(); i++) {
            s1[st[cur][i]]--;
        }
        
        for (int i = 0; i < st[cur].size(); i++) {
            s2[st[cur][i]]++;
        }
        dfs(cur+1);
        for (int i = 0; i < st[cur].size(); i++) {
            s2[st[cur][i]]--;
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; kase++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            st[i].clear();
        }
        sts.clear();
        memset(s1, 0, sizeof(s1));
        memset(s2, 0, sizeof(s2));
        string line, s;
        getline(cin, line);
        getline(cin, line);
        stringstream ss(line);
        while (ss >> s) {
            s1[hs(s)]++;
            sts.insert(hs(s));
            // printf("E: %s\n", s.c_str());
        }
        getline(cin, line);
        stringstream ss2(line);
        while (ss2 >> s) {
            s2[hs(s)]++;
            sts.insert(hs(s));
            //   printf("F: %s\n", s.c_str());
        }
        n -= 2;
        for (int i = 0; i < n; i++) {
            getline(cin, line);
            stringstream ss3(line);
            while (ss3 >> s) {
                sts.insert(hs(s));
                st[i].push_back(hs(s));
            }
        }
        ans = 1<<30;
        //for (auto i: sts) printf("%lld\n", i);
        dfs(0);
        printf("Case #%d: %d\n", kase, ans);
    }
    return 0;
}
