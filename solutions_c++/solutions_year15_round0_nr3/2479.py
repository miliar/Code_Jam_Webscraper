#include <iostream>
#include <cstdio>
#include <string>
#include <map>

using namespace std;

map<pair<char, char>, pair<char, bool> > mul_table;

void init() {
    mul_table[{'1', '1'}] = {'1', false};
    mul_table[{'1', 'i'}] = {'i', false};
    mul_table[{'1', 'j'}] = {'j', false};
    mul_table[{'1', 'k'}] = {'k', false};

    mul_table[{'i', '1'}] = {'i', false};
    mul_table[{'i', 'i'}] = {'1', true};
    mul_table[{'i', 'j'}] = {'k', false};
    mul_table[{'i', 'k'}] = {'j', true};

    mul_table[{'j', '1'}] = {'j', false};
    mul_table[{'j', 'i'}] = {'k', true};
    mul_table[{'j', 'j'}] = {'1', true};
    mul_table[{'j', 'k'}] = {'i', false};

    mul_table[{'k', '1'}] = {'k', false};
    mul_table[{'k', 'i'}] = {'j', false};
    mul_table[{'k', 'j'}] = {'i', true};
    mul_table[{'k', 'k'}] = {'1', true};
}

pair<char, bool> mul(pair<char, bool> a, pair<char, bool> b) {
    pair<char, bool> res = mul_table[{a.first, b.first}];
    res.second ^= (a.second ^ b.second);
    return res;
}

const int maxlen = 10005;

pair<char, bool> d[maxlen][maxlen];

int main() {
    init();
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int L, X;
        cin >> L >> X;
        string tmp;
        cin >> tmp;
        string s;
        for (int i = 0; i < X; ++i)
            s += tmp;
        
        for (int i = 0; i < s.size(); ++i) {
            d[i][i] = {s[i], false};
            for (int j = i + 1; j < s.size(); ++j) {
                d[i][j] = mul(d[i][j - 1], {s[j], false});
            }
        }

        bool flag = false;

        for (int p1 = 1; p1 < s.size(); ++p1) {
            if (d[0][p1 - 1] != make_pair('i', false))
                continue;
            for (int p2 = p1 + 1; p2 < s.size(); ++p2) {
                pair<char, bool> c1 = d[0][p1 - 1];
                pair<char, bool> c2 = d[p1][p2 - 1];
                pair<char, bool> c3 = d[p2][s.size() - 1];
                if (c1 == make_pair('i', false) && c2 == make_pair('j', false) && 
                            c3 == make_pair('k', false)) {
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }

        printf("Case #%d: %s\n", test, (flag ? "YES" : "NO"));

    }
}
