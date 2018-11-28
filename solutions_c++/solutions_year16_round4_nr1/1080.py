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
#include <complex>

using namespace std;

vector<int> get(int N, int st) {
    vector<int> d;
    d.push_back(st);
    for (int i = 0; i < N; i++) {
        vector<int> s;
        for (int j = 0; j < d.size(); j++) {
            if (d[j] == 1) {
                s.push_back(1); s.push_back(2);
            }
            if (d[j] == 2) {
                s.push_back(3); s.push_back(2);
            }
            if (d[j] == 3) {
                s.push_back(3); s.push_back(1);
            }
        }
        d = s;
    }
    return d;
}

string sorting(vector<int> a) {
    vector<string> s;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] == 1) s.push_back("R");
        if (a[i] == 2) s.push_back("S");
        if (a[i] == 3) s.push_back("P");
    }
    while (s.size() != 1) {
        vector<string> q;
        int i = 0;
        while (i < s.size()) {
            string g1 = s[i] + s[i + 1];
            string g2 = s[i + 1] + s[i];
            if (g1 < g2) q.push_back(g1);
            else q.push_back(g2);
            i += 2;
        }
        s = q;
    }
    return s[0];
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        string pans = "";
        int N, R, P, S;
        cin >> N >> R >> P >> S;
        cout << "Case #" << test << ": ";
        vector<int> ans1 = get(N, 1);
        vector<int> ans2 = get(N, 2);
        vector<int> ans3 = get(N, 3);
        //----------------
        int R1 = 0, P1 = 0, S1 = 0;
        for (int i = 0; i < ans1.size(); i++) {
            if (ans1[i] == 1) R1++;
            if (ans1[i] == 2) S1++;
            if (ans1[i] == 3) P1++;
        }
        if (R1 == R && P1 == P && S1 == S) {
            string q = sorting(ans1);
            pans = q;
            /*for (int i = 0; i < ans1.size(); i++) {
                if (ans1[i] == 1) cout << "R";
                if (ans1[i] == 2) cout << "P";
                if (ans1[i] == 3) cout << "S";
            }*/
        }
        //----------------
        R1 = 0, P1 = 0, S1 = 0;
        for (int i = 0; i < ans2.size(); i++) {
            if (ans2[i] == 1) R1++;
            if (ans2[i] == 2) S1++;
            if (ans2[i] == 3) P1++;
        }
        if (R1 == R && P1 == P && S1 == S) {
            string q = sorting(ans2);
            if (q < pans || pans == "")pans = q;
            /*for (int i = 0; i < ans2.size(); i++) {
                if (ans2[i] == 1) cout << "R";
                if (ans2[i] == 2) cout << "P";
                if (ans2[i] == 3) cout << "S";
            }*/
        }
        //----------------
        R1 = 0, P1 = 0, S1 = 0;
        for (int i = 0; i < ans3.size(); i++) {
            if (ans3[i] == 1) R1++;
            if (ans3[i] == 2) S1++;
            if (ans3[i] == 3) P1++;
        }
        if (R1 == R && P1 == P && S1 == S) {
            string q = sorting(ans3);
            if (q < pans || pans == "")pans = q;
            /*for (int i = 0; i < ans3.size(); i++) {
                if (ans3[i] == 1) cout << "R";
                if (ans3[i] == 2) cout << "P";
                if (ans3[i] == 3) cout << "S";
            }*/
        }
        if (pans != "") cout << pans << endl;
        else cout << "IMPOSSIBLE\n";
    }
}

