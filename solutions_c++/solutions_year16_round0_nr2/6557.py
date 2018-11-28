//
//  main.cpp
//  RevengeOfThePancakes
//
//  Created by 강대원 on 2016. 4. 9..
//  Copyright © 2016년 강대원. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#define M 100

using namespace std;

void reverse(bool &value) {
    value = !value;
}

int RevengeOfThePancakes(string S) {
    int i, j, n = S.length(), k;
    int result = 0;
    bool s[M];
    for (i = 0; i < n; i++) {
        s[i] = S[i] == '+' ? true : false;
    }
    for (i = n - 1; i >= 0; i--) {
        if (s[i]) continue;
        result += 1;
        for (j = 0; j <= i; j++) {
            if (s[j] != s[0]) {
                break;
            }
        }
        
        if (s[0]) {
            result += 1;
            for (k = 0; k < j; k++) {
                reverse(s[k]);
            }
        }
        
        for (j = i; j >= (float)i / 2; j--) {
            if (j == (i - j)) {
                reverse(s[j]);
            } else {
                reverse(s[j]);
                reverse(s[i - j]);
            }
            swap(s[j], s[i - j]);
        }
    }
    return result;
}

int main(int argc, const char * argv[]) {
    ifstream in("input.in");
    ofstream out("output.out");
    int T, i;
    string S;
    in >> T;
    for (i = 0; i < T; i++) {
        in >> S;
        out << "Case #" << i + 1 << ": " << RevengeOfThePancakes(S) << endl;
    }
    return 0;
}