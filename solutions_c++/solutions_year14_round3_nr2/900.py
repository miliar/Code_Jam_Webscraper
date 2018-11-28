#include <iostream>
#include <string>
#include <vector>
#include <deque>
using namespace std;

bool can(const vector<string> & s, int x, int y) {
    char last=' ';
    vector<bool> app(26, false);
    for (x=x<0?0:x; x<=y; ++x) {
        for (int i=0, N=s[x].size(); i<N; ++i) {
            if (app[s[x][i]-'a'] && s[x][i]!=last)
                return false;
            last=s[x][i];
            app[s[x][i]-'a'] = true;
        }
    }
    return true;
}

bool can(const vector<string> & ss) {
    return can(ss, 0, ss.size()-1);
}

vector<vector<string>>bfs(const vector<string> &ss) {
    deque<vector<string>>que;
    if (!ss.empty()) {
        vector<string> x = vector<string>{ss[0]};
        if (can(x))
            que.push_back(x);
    }
    for (int i=1, N=ss.size(); i<N; ++i)
        for (int j=que.size()-1; j>=0; --j) {
            vector<string> t=que.front();
            que.pop_front();
            t.push_back(ss[i]);
            if (can(t)) {
                que.push_back(t);
            }
            for (int k=t.size()-2; k>=0; --k) {
                swap(t[k], t[k+1]);
                if (!can(t, k-1, k+1)) continue;
                que.push_back(t);
            }
        }
    return vector<vector<string>>(que.begin(), que.end());
}

int solve(vector<string> ss) {
    int ans=0;
    vector<vector<string>> all = bfs(ss);
    for (auto ns : all) {
        if (can(ns)) ++ans;
    }
    return ans;
}

int main() {
    int casenum; cin>>casenum;
    for (int casei=1; casei<=casenum; ++casei) {
        int N; cin >> N;
        vector<string> s(N);
        for (int i=0; i<N; ++i) {
            cin >> s[i];
        }
        int ans = solve(s);
        cout << "Case #" << casei << ": " << ans << endl;
    }
    return 0;
}
