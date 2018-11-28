/*
 * test.cpp
 * Copyright (C) 2016 Jiahao Wu <visylar@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <map>
#include <set>
#include <string>
#include <cstring>

using namespace std;

const string numbers[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int chcnt[30];
int outnumber[700];
int oindex;
bool done=false;

void search(int remain) {
    if(done) return;
    if(remain == 0) {
        for (int i = 0; i < oindex; ++i) {
            cout << outnumber[i];
        }
        done = true;
        return;
    }
    for (int i = 0; i < 10; ++i) {
        bool isOk = true;
        for(unsigned long j = 0; j < numbers[i].length(); ++j) {
            chcnt[numbers[i].at(j) - 'A']--;
            if(chcnt[numbers[i].at(j) - 'A'] < 0) {
                isOk = false;
            }
        }
        if(isOk) {
            outnumber[oindex++] = i;
            search(remain-numbers[i].length());
            oindex--;
        }
        for(unsigned long j = 0; j < numbers[i].length(); ++j) {
            chcnt[numbers[i].at(j) - 'A']++;
        }
    }
}

void solve() {
    memset(outnumber, 0, sizeof(outnumber));
    oindex = 0;
    string str;
    cin >> str;
    memset(chcnt, 0, sizeof(chcnt));
    for (auto ch : str) {
        chcnt[ch - 'A']++;
    }
    int chtotal = str.length();
    search(chtotal);
}

int main(/*int argc, char *argv[]*/) {

    int T;
    ios::sync_with_stdio(false);
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << i + 1 << ": ";
        done=false;
        solve();
        cout << endl;
    }
    return 0;
}
