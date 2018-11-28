//
//  main.cpp
//  pa
//
//  Created by Rongbin Li on 4/30/16.
//  Copyright © 2016 Rongbin Li. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cassert>
using namespace std;

const string dig[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
const char idc[10] = {'Z', 'O', 'W', 'T', 'U', 'F', 'X', 'S', 'G', 'I'};

void addCount(char c, int x, int count[]) {
    count[c-'A'] += x;
}

void getCount(int num[], int n, int count[], int ans[]) {
    for (int i=0; i<n; i++) {
        int d = num[i];
        int x = count[idc[d] -'A'];
        ans[d] = x;
        for (int j=0; j<dig[d].size(); j++) {
            count[dig[d][j]-'A'] -= x;
        }
    }
}

string getAns(string s) {
    int count[26] = {0};
    int ans[10] = {0};
    for (int i=0; i<s.size(); i++) {
        count[s[i]-'A']++;
    }
    
    int num1[] = {0, 2, 4, 6, 8};
    getCount(num1, 5, count, ans);
    int num2[] = {1, 3, 5, 7};
    getCount(num2, 4, count, ans);
    ans[9] = count['I'-'A'];
    string ret;
    for (int i=0; i<=9; i++) {
        ret.append(ans[i], '0'+i);
    }
    return ret;
}

int main(int argc, const char * argv[]) {
    ifstream fin("A-large.in");
    assert(fin);
    ofstream fout("pa-large.out");
    assert(fout);
    int test;
    fin >> test;
    for (int c = 1; c<=test; c++) {
        string s;
        fin >> s;
        fout << "Case #" << c << ": " << getAns(s) << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
