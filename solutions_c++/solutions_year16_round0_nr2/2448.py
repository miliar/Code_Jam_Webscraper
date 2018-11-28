#define _CRT_SECURE_NO_WARNINGS

#pragma comment(linker, "/STACK:16777216")
#include <cmath>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <time.h>
#include <iomanip>
#include <cstdio>

using namespace std;


int  main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    string s;
    getline(cin, s);
    for (int test = 1; test <= tests; test++) {
        getline(cin, s);
        int p = 0;
        if (s[0] == '-') p = 1;
        int ans = 0;
        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] == '+' && s[i + 1] == '-') ans++;
        }
        cout << "Case #" << test << ": " << ans * 2 + p << endl;
    }
    
}