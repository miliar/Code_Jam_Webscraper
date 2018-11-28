//
//  main.cpp
//  test
//
//  Created by Haoliang on 7/27/15.
//  Copyright (c) 2015 Haoliang. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <vector>
#include <mutex>
#include <sstream>
#include <algorithm>
#include <string>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <map>
#include <set>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <thread>
#include <bitset>
#include <cmath>
#include <fstream>
#include <iterator>
#include <inttypes.h>

using namespace std;

unordered_map<int, string> dic = {{0, "ZERO"}, {1, "ONE"}, {2, "TWO"}, {3, "THREE"},
    {4, "FOUR"}, {5, "FIVE"}, {6, "SIX"}, {7, "SEVEN"}, {8, "EIGHT"}, {9, "NINE"}};

bool dfs(unordered_map<char, int>& mp, string& res, int i) {
    bool ret = true;
    for (auto& p : mp) {
        if (p.second > 0) {
            ret = false;
            break;
        }
    }
    if (ret) {
        return true;
    }else if (i == 10) {
        return false;
    }
    unordered_map<char, int> tmp;
    for (char c : dic[i]) {
        tmp[c]++;
    }
    bool f = true;
    int ttl = 0;
    while (f) {
        for (auto& p : tmp) {
            char x = p.first;
            int cnt = p.second;
            if (mp[x] < cnt) {
                f = false;
                break;
            }
        }
        if (f) {
            ttl++;
            res.push_back(i + '0');
            for (auto& p : tmp) {
                char x = p.first;
                int cnt = p.second;
                mp[x] -= cnt;
            }
        }
    }
    if (dfs(mp, res, i + 1)) {
        return true;
    }else {
        while (ttl > 0) {
            ttl--;
            res.pop_back();
            for (auto& p : tmp) {
                char x = p.first;
                int cnt = p.second;
                mp[x] += cnt;
            }
            if (dfs(mp, res, i + 1)) {
                return true;
            }
        }
    }
    return false;
}

int main(){
    unordered_map<char, int> mp;
    ifstream fin("/Users/haoliang/Desktop/A-small-attempt3.in");
    ofstream fout("/Users/haoliang/Desktop/A-small-attempt3.out");
    string line;
    int x = 0;
    while (getline(fin, line)) {
        x++;
        if (x == 1) {
            continue;
        }
        mp.clear();
        for (int i = 0; i < line.size(); ++i) {
            mp[line[i]]++;
        }
        string res;
        dfs(mp, res, 0);
        fout << "Case #" << x - 1 << ": " << res << endl;
    }
    fin.close();
    fout.close();
}