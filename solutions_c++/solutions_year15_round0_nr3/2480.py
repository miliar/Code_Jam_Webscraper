#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

char s[10005];
void reduce(pair<bool,char> & cur, char c) {
    if (cur.second == '1') cur.second = c;
    else if (cur.second == c) {
        cur.second = '1';
        cur.first = !cur.first;
    } else if (cur.second == c) {
        cur.first = !cur.first;
        cur.second = '1';
    } else if (cur.second == 'i') {
        if (c == 'j') cur.second = 'k';
        else {
            cur.second = 'j';
            cur.first = !cur.first;
        }
    } else if (cur.second == 'j') {
        if (c == 'i') {
            cur.second = 'k';
            cur.first = !cur.first;
        } else cur.second = 'i';
    } else if (cur.second == 'k') {
        if (c == 'i') cur.second = 'j';
        else {
            cur.second = 'i';
            cur.first = !cur.first;
        }
    }
}
void print_pair(pair<bool,char> p) {
    cout << '(' << p.first << ',' << p.second << ')';
}
void deduce(char c, pair<bool, char> & cur) {
    if (c == cur.second) {
        cur.second = '1';
        return;
    } else if (cur.second == '1') {
        cur.first = !cur.first;
        cur.second = c;
        return;
    }
    switch (c) {
        case 'i':
            switch (cur.second) {
                case 'j':
                    cur = {!cur.first, 'k'};
                    break;
                case 'k':
                    cur = {cur.first, 'j'};
                    break;
                default:
                    break;
            }
            break;
        case 'j':
            switch (cur.second) {
                case 'i':
                    cur = {cur.first, 'k'};
                    break;
                case 'k':
                    cur = {!cur.first, 'i'};
                    break;
                default:
                    break;
            }
            break;
        case 'k':
            switch (cur.second) {
                case 'i':
                    cur = {!cur.first, 'j'};
                    break;
                case 'j':
                    cur = {cur.first, 'i'};
                    break;
                default:
                    break;
            }
            break;
        default:
            break;
    }
}

inline bool ispos(bool a, bool b, bool c) {
    bool ret = true;
    if (!a) ret = !ret;
    if (!b) ret = !ret;
    if (!c) ret = !ret;
    return ret;
}
bool can_be_reduced(const string & str) {
    pair<bool,char> fir= {true,'1'};
    vector<pair<bool,char>> last_vec;
    for (auto c : str) {
        reduce(fir, c);
    }
    for (auto c : str) {
        last_vec.push_back(fir);
        deduce(c, fir);
    }
    if (fir!= make_pair(true, '1')) {
        puts("ERROR");
    }
    for (int i = 0; i < str.size()-2; ++i) {
        reduce(fir, str[i]);
        if (fir.second == 'i') {
            pair<bool,char> sec = {true,'1'};
            for (int j = i+1; j < str.size()-1; ++j) {
                reduce(sec, str[j]);
                if (sec.second == 'j' && last_vec[j+1].second == 'k') {
                    pair<bool,char> thi = last_vec[j+1];
                    if (ispos(fir.first,sec.first,thi.first)) {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    freopen("/Users/wenzhengjiang/Downloads/C-small-attempt3.in", "r", stdin);
    freopen("/Users/wenzhengjiang/Documents/CppPrimer/CppPrimer/C-small.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int ncase = 1; ncase <= t; ncase++) {
        int L, X;
        scanf("%d%d", &L, &X);
        scanf("%s", s);
        string str(s);
        while (--X) str += s;
        if (can_be_reduced(str))
            printf("Case #%d: YES\n",ncase);
        else
            printf("Case #%d: NO\n",ncase);
        
    }
    fclose(stdout);
}