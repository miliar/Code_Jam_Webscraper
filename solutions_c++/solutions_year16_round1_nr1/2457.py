#include <string>
#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
    int ncase;
    cin >> ncase;
    for (int ic=0; ic<ncase; ++ic) {
        string s;
        cin >> s;
        string res;
        for (auto ch : s)
            if (res == "") res.push_back(ch);
            else if (ch >= res.front()) res = ch + res;
            else res.push_back(ch);
        printf("Case #%d: %s\n", ic+1, res.c_str());
    }
    return 0;
}