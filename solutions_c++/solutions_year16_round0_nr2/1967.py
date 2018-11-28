/**
 * file: pancake.cpp
 * @author: Yangmu Jiang
 * @mail: celsius.j@gmail.com
 * @created time: Apr 08 2016
 */

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int flipcake(string &s) {
    int flip = s.back() == '-' ? 1 : 0;
    const char *p = (s.c_str() + s.size()) - 2;
    const char *end = s.c_str();
    while (p >= end) {
        if (*p != *(p+1))
            ++flip;
        --p;
    }
    return flip;
}
    
int main(int argc, char **argv)
{
    int test = 0;
    string s;
    cin >> test;
    for (int i = 1; i <= test; ++i) {
        cin >> s;
        cout << "Case #" << i << ": " << flipcake(s) << endl;
    }
    return 0;
}

