#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

string dfs(string s) {
    string s_cp = s;
    //vector <pair <char, > >
    sort(s_cp.begin(), s_cp.end(), greater<char>());
    char c = s_cp[0];
    int c_cnt = 0;
    while (s_cp[c_cnt] == c) {
        c_cnt++;
    }
    int minn_idx = -1;
    int len = s.size();
    for (int i = 0; i < len; i++) {
        if (s[i] == c) {
            minn_idx = i;
            break;
        }
    }
    if (minn_idx == 0) {
        string res;
        for (int i = 0; i < len; i++) {
            if (s[i] != c) {
                res = res + s[i];
            }
        }
        string start(c_cnt, c);
        return start + res;
    }
    else {
        string second = s.substr(0, minn_idx);
        string second_res = dfs(second);
        string res;
        for (int i = minn_idx; i < len; i++) {
            if (s[i] != c) {
                res = res + s[i];
            }
        }
        string start(c_cnt, c);
        return start + second_res + res;
    }
}

int main() {
    int T = 0, cnt = 0;
    cin>>T;
    while (T--) {
        cnt++;
        string s;
        cin>>s;
        //s_cp = s;
        string res = dfs(s);
        printf("Case #%d: %s\n", cnt, res.c_str());
    }
    return 0;
}
