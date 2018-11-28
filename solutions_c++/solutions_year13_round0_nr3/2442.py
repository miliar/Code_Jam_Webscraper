#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

bool isPalindrome(const string& str) {
    string rev = str;
    reverse(rev.begin(), rev.end());
    return (str == rev);
}

int main(void) {
    vector<int> palindromes;
    for (int j = 1; j <= 9999; ++j) {
        char str[9];
        sprintf(str, "%d", j);
        int l = strlen(str);
        for (int i = l; i < 2*l; ++i) {
            str[i] = str[2*l - i - 1];
        }
        str[2*l] = 0;
        int t;
        sscanf(str, "%d", &t);
        palindromes.push_back(t);
        for (int i = l; i < 2*l - 1; ++i) {
            str[i] = str[2*l - i - 2];
        }
        str[2*l - 1] = 0;
        sscanf(str, "%d", &t);
        palindromes.push_back(t);
    }
    vector<long long> res;
    for each (int pal in palindromes) {
        long long t= pal * (long long)pal;
        char str[19];
        sprintf(str, "%lld", t);
        if (isPalindrome(str))
            res.push_back(t);
    }
    sort(res.begin(), res.end());
    int T;
    cin >> T;
    for (int testNo = 1; testNo <= T; ++testNo) {
        long long A, B;
        cin >> A >> B;
        auto it1 = lower_bound(res.begin(), res.end(), A);
        auto it2 = upper_bound(res.begin(), res.end(), B);
        cout << "Case #" << testNo << ": " << it2 - it1 << endl;
    }
    return 0;
}
