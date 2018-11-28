/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2015/04/11 19时40分19秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <cstdio>
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int t;
    cin >> t;
    int tt = 0;
    int m;
    string s;
    for (; t; --t) {
        cin >> m >> s;
        int tmp = 0, ans = 0;
        for (int i = 0; i <= m; ++i) {
            if (tmp < i) {
                ans = ans + i - tmp;
                tmp = i;
            }
            tmp = tmp + s[i] - '0';
        }
        cout << "Case #" << ++tt << ": " << ans << endl; 
    }
}

