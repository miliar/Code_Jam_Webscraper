#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;
vector<string> ans;
bool cmp(const string &a, const string &b) {
    return a.compare(b) > 0;
}

int main() {
    int T;
    int test_case;

    scanf("%d",&T);
    for(test_case = 1; test_case <= T; test_case++) {
        string word;
        ans.clear();
        queue<string> q;
        cin >> word;
        if(word.size() == 1) {
            printf("Case #%d: %s\n", test_case,word.c_str());
            continue;
        }
        int strSize = word.size();
        int idx = 0;
        string temp;
        temp += word[idx++];
        q.push(temp);
        while(idx != strSize) {
            queue<string> newq;
            while(!q.empty()) {
                string str = q.front(); q.pop();
                string pre = word[idx] + str;
                string post = str + word[idx];
                if(pre.size() == strSize) {
                    ans.push_back(pre);
                    ans.push_back(post);
                }
                newq.push(pre); newq.push(post);
            }
            idx++;
            q = newq;
        }
        sort(ans.begin(), ans.end(), cmp);
        printf("Case #%d: %s\n", test_case,ans[0].c_str());
    }
    return 0;
}


