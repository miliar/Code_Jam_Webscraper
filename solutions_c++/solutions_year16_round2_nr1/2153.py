/* 
 * File:   main.cpp
 * Author: juro
 *
 * Created on April 30, 2016, 6:05 PM
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

/*
 * 
 */
map<int, string> numbers = {{0, "ZERO"}, {1, "ONE"}, {2, "TWO"}, {3, "THREE"}, {4, "FOUR"}, {5, "FIVE"}, {6, "SIX"}, {7, "SEVEN"}, {8, "EIGHT"}, {9, "NINE"}};

vector<int> order = {0,2,4,6,8,3,1,5,7,9};

map<char, int> get_stats(string s) {
    map<char, int> res;
    for (int i = 0; i < s.size(); i++) res[s[i]] = res[s[i]] + 1;
    return res;
}

bool rem_num(map<char, int> &stat, int num) {
    string strnum = numbers[num];
    map<char, int> stat_num = get_stats(strnum);
    for (auto it : stat_num) {
        if (it.second > stat[it.first]) return false;
    }
    for (auto it : stat_num) {
        stat[it.first] -= it.second;
    }
    return true;
}

bool try_str(map<char, int> &stat, vector<int> &res) {
    bool hassol = false;
    bool empt = true;
    for (auto it : stat) {
        if (it.second > 0) empt = false;
    }
//    cout << empt << endl;
    if (empt) return true;
    for (int i = 0; i < order.size(); i++) {
        if (rem_num(stat, order[i])) {
            if (try_str(stat, res)) {
                res.push_back(order[i]);
                hassol = true;
            }
        }
    }
    return hassol;
}

int main(int argc, char** argv) {

    int t;
    cin >> t;
    
    for (int i = 0; i< t; i++) {
        string s;
        cin >> s;
        vector<int> res;
        map<char, int> stat = get_stats(s);
        try_str(stat, res);
        sort(res.begin(), res.end());
        printf("Case #%d: ", i+1);
        for (int j = 0; j < res.size(); j++) cout << res[j];
        cout << endl;
    }
    
    return 0;
}

