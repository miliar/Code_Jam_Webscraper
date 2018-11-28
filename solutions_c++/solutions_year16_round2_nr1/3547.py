#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

vector<int> nums;

vector<string> digits = {
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX",
    "SEVEN", "EIGHT", "NINE"
};

bool judge(int idx, unordered_map<char, int>& umap) {
    bool flag = true;
    for(int i = 0; i < digits[idx].size(); ++ i) {
        if(umap[digits[idx][i]] <= 0) flag = false;
    }
    return flag;
}

void decr(int idx, unordered_map<char, int>& umap) {
    for(int i = 0; i < digits[idx].size(); ++ i)
        umap[digits[idx][i]] --;
}

void incr(int idx, unordered_map<char, int>& umap) {
    for(int i = 0; i < digits[idx].size(); ++ i)
        umap[digits[idx][i]] ++;
}

void dfs(vector<int>& tmp, int cnt, bool& flag, unordered_map<char, int>& umap)
{
    if(cnt < 0) return;
    if(flag) return;
    if(cnt == 0) {
        for(int i = 0; i < tmp.size(); ++ i)
            nums.push_back(tmp[i]);
        flag = true;
        return;
    }
    for(int i = 1; i < 10; ++ i) {
        if(judge(i, umap)) {
            //cout << i << " -- " << cnt << endl;
            tmp.push_back(i);
            decr(i, umap);
            dfs(tmp, cnt - digits[i].size(), flag, umap);
            tmp.pop_back();
            incr(i, umap);
        }
    }
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("outS.txt", "w", stdout);
    int tcase;
    string str;
    cin >> tcase;
    for(int i = 1; i <= tcase; ++ i){
        cin >> str;
        unordered_map<char, int> umap;
        nums.clear();
        for(int i = 0; i < str.size(); ++ i) {
            umap[str[i]] ++;
        }

        int cnt = umap['Z'];
        for(int i = 0; i < cnt; ++ i) {
            nums.push_back(0);
            umap['Z'] --;
            umap['O'] --;
            umap['E'] --;
            umap['R'] --;
        }

        bool flag = false;
        vector<int> tmp;
        dfs(tmp, str.size() - cnt*4, flag, umap);
        cout << "Case #" << i << ": ";
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); ++ i)
            cout << nums[i];
        cout << endl;
    }
    return 0;
}
