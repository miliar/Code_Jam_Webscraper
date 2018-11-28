//
// Created by 冯斯聪 on 16/4/15.
//

#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

vector<int> solve(string s) {
    vector<int> res(10, 0);
    map<int, char> m1 = {{0,'Z'},{2,'W'},{4,'U'},{6,'X'}, {8,'G'}};
    map<int, char> m2 = {{1,'O'}, {3,'H'}, {5, 'F'}, {7, 'S'}};
    map<int, char> m3 = {{9,'I'}};
    map<int, string> m = {{0,"ZERO"}, {1,"ONE"}, {2,"TWO"}, {3,"THREE"}, {4,"FOUR"},
                          {5,"FIVE"},{6,"SIX"}, {7,"SEVEN"}, {8,"EIGHT"}, {9,"NINE"}};

    map<char, int> in;
    for (int i = 0; i < s.length(); ++i) {
        in[s[i]]++;
    }
    for (auto it = m1.begin(); it != m1.end(); it++) {
        if (in.count(it->second) && in[it->second] != 0) {
            int dig = it->first;
            int rep = in[it->second];
            res[dig] = rep;
            string num = m[dig];
            for (int i = 0; i < num.length(); ++i) {
                in[num[i]] -=rep;
            }
        }
    }
    for (auto it = m2.begin(); it != m2.end(); it++) {
        if (in.count(it->second) && in[it->second] != 0) {
            int dig = it->first;
            int rep = in[it->second];
            res[dig] = rep;
            string num = m[dig];
            for (int i = 0; i < num.length(); ++i) {
                in[num[i]] -=rep;
            }
        }
    }
    for (auto it = m3.begin(); it != m3.end(); it++) {
        if (in.count(it->second) && in[it->second] != 0) {
            int dig = it->first;
            int rep = in[it->second];
            res[dig] = rep;
            string num = m[dig];
            for (int i = 0; i < num.length(); ++i) {
                in[num[i]] -=rep;
            }
        }
    }
    return res;
}



int main(void) {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        string s;
        cin >> s;
        vector<int> out = solve(s);
        cout << "Case #" << i+1 <<": ";
        for (int j = 0; j < 10; ++j) {
            for (int k = 0; k < out[j]; ++k) {
                cout << j;
            }
        }
        cout << endl;
    }

    return 0;
}