#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>

#define mp make_pair

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

vector<string> v;
vector<vector<int> > t;
int n, m;
int worst, num;

int calc() {
    int i, j, k, res;
    res = n;
    set<string> s;
    for(i=0; i<n; ++i) {
        s.clear();
        for(j=0; j<t[i].size(); ++j) {
            for(k=1; k<=v[t[i][j]].size(); ++k) {
                s.insert(v[t[i][j]].substr(0, k));
            }
        }
        res += s.size();
    }
    return res;
}

void rec(int cur) {
    if (cur == m) {
        for(int i=0; i<n; ++i) {
            if (t[i].empty()) return;
        }
        int temp = calc();
        if (temp > worst) {
            worst = temp;
            num = 1;
        } else if (temp == worst) {
            ++num;
        }
        return;
    }
    for(int i=0; i<n; ++i) {
        t[i].push_back(cur);
        rec(cur+1);
        t[i].pop_back();
    }
    return;
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int i, j;
    int T, NT;
    cin>>NT;
    for(T = 1; T <= NT; ++T) {
        cin>>m>>n;
        v.clear();
        v.resize(m);
        for(i=0; i<m; ++i) {
            cin>>v[i];
        }
        t.clear();
        t.resize(n);
        worst = num = 0;
        rec(0);
        printf("Case #%d: %d %d\n", T, worst, num);
    }
    return 0;
}
