//
// Created by 冯斯聪 on 16/4/9.
//
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string rev(string &s) {
    int len = s.length();
    string ret(len, '+');
    for (int i = 0; i < len; ++i) {
        ret[len-i-1] = (s[i]=='+')?'-':'+';
    }
    return ret;
}

int countFlips(string s) {
    int len = s.length();
    if (len==0) return 0;
    if (s[len-1]=='+') {
        int i=len;
        while (s[i-1]=='+') i--;
        return countFlips(s.substr(0, i));
    }
    else {
        if (s[0]=='-') {
            string re = rev(s);
            return countFlips(re)+1;
        }
        else {
            int i=0;
            while (s[i]=='+') i++;
            string into = s.substr(0,i);
            string pre = rev(into);
            for (int j = 0; j < i; ++j) {
                s[j] = pre[j];
            }
            return countFlips(s)+1;
        }
    }
}


int main(void) {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        string s;
        cin >> s;
        int ret = countFlips(s);
        cout << "Case #" << i+1 << ": ";
        cout << ret << endl;
    }
    return 1;
}