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
    int test;
    cin >> test;
    int n, k;
    cin >> n >> k;
    int ans = 0;
    cout << "Case #1:\n";
    for (int j = 0; j < 1100000000; j++) {
        string s = "";
        int x = j;
        while (x > 0) {
            s = (char)(x % 2 + 48) + s;
            x /= 2;
        }
        while (s.size() < n - 2) {
            s = '0' + s;
        }
        s = "1" + s + "1";
        if (s.size() != n) continue;
        bool is = true;
        int q = 0;
        int k1 = 0, k2 = 0;
        for (int i = 0; i < s.size(); i++)
            if (s[i] == '1') {
                q++;
                if (i % 2 == 0) k1++;
                if (i % 2 == 1) k2++;
            }
        if (q % 2 == 1 || k1 != k2) is = false;

        if (is) {
            ans++;
            cout << s << " ";
            for (int i = 2; i <= 10; i++) {
                if (i % 2 == 0) cout << i + 1 << " ";
                else cout << 2 << " ";
            }
            cout << endl;
        }
        if (ans == k) break;
    }
    
}