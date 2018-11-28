/*
HACK ME IF YOU CAN!
░░███▒▒░░░░░░░░░░░░░░░░████
░░████▒░░░░░░░░░░░░░░░███▒█
░░██████░░░░░░░░░░░░░███▒▒▒█
░░██▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█████▒██
░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▒▒▒░██
▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒█
▒▒▓▓███████▓░▓▓███████▓▒▒▒▒▒▒
▒▒▓▓▓█▓▄▓█▓░░░▓▓█▓▄▓█▓▓▒▒▒▒▒▒
▒▒▓▓▓▓███▓░░░░░▓▓███▓▓▓▒▒▒▒▒▒
▒▒▒▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒
▒▒▒▒▓▓▓▓▓▒██▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░▒▒▒▒▒▒▒▒█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
*/
#include <iostream>
#include <stdio.h>
#include <vector>
#include <bits/stdc++.h>
#include <map>
#include <climits>
#include <cstring>
#include <algorithm>
#include <set>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
//#include <ext/pb_ds/detail/standard_policies.hpp>
#define mp make_pair
#define pb push_back
#define fc first
#define sc second
#define all(x) x.begin(), x.end()
#define ll long long
#define ld long double
#define min(a, b) (a < b ? a : b)
#define cost fc
#define u sc.fc.fc
#define v sc.fc.sc
#define ind sc.sc
 
using namespace std;
 
map <char, int> c;

bool ok(string s) {
    int cnt = 0;
    map <char, int> p;
    for (int i = 0; i < (int) s.size(); i++) {
        p[s[i]]++;
    }
    for (int i = 0; i < (int) s.size(); i++) {
        if (c[s[i]] < p[s[i]]) {
            return 0;
        }
    }
    return 1;
}

void dec(string s) {
    for (int i = 0; i < (int) s.size(); i++) {
        c[s[i]]--;
    }
}

int ans[10];

int main() {
    #ifdef __linux__
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    #ifndef __linux__
        //freopen("towers.in", "r", stdin);
        //freopen("towers.out", "w", stdout);
    #endif
    int t;
    cin >> t;
    int cnt = 0;
    while (t--) {
        cnt++;
        string s;
        cin >> s;
        c.clear();
        for (int i = 0; i < 10; i++) {
            ans[i] = 0;
        }
        for (int i = 0; i < (int) s.size(); i++) {
            c[s[i]]++;
        }
        while (ok("ZERO")) {
            dec("ZERO");
            ans[0]++;
        }
        while (ok("TWO")) {
            dec("TWO");
            ans[2]++;
        }
        while (ok("FOUR")) {
            dec("FOUR");
            ans[4]++;
        }
        while (ok("THREE")) {
            dec("THREE");
            ans[3]++;
        }
        while (ok("ONE")) {
            dec("ONE");
            ans[1]++;
        }
        while (ok("FIVE")) {
            dec("FIVE");
            ans[5]++;
        }
        while (ok("SEVEN")) {
            dec("SEVEN");
            ans[7]++;
        }
        while (ok("SIX")) {
            dec("SIX");
            ans[6]++;
        }
        while (ok("EIGHT")) {
            dec("EIGHT");
            ans[8]++;
        }
        while (ok("NINE")) {
            dec("NINE");
            ans[9]++;
        }
        cout << "Case #" << cnt << ": ";
        for (int i = 0; i < 10; i++) {
            while (ans[i] > 0) {
                cout << i;
                ans[i]--;
            }
        }
        cout << endl;
    }
}