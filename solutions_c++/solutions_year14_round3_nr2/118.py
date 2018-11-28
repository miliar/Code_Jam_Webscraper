#include <iostream>
#include <stdio.h>
#include <vector>
#include <string.h>
#include <sstream>

using namespace std;

int T, N, caseNumber = 1, v[110];
long long MOD = 1000000007, F[110];
int all(string s, char ch) {
    for(int i = 0; i < s.size(); i++) {
        if (s[i] != ch) return false;
    }
    return true;
}
int pre(string s, char ch) {
    if (s[0] == ch) return true;
    else return false;
}
int suf(string s, char ch) {
    if (s[s.size() - 1] == ch) return true;
    else return false;
}
int con(string s, char ch) {
    for(int i = 0; i < s.size(); i++) {
        if (s[i] == ch) return true;
    }
    return false;
}
int good(string s, char ch) {
    int prev = 0, cnt = 0;
    for(int i = 0; i < s.size(); i++) {
        if (s[i] == ch) {
            if (!prev) {prev = 1; cnt++;}
        } else prev = 0;
    }
    return cnt <= 1;
}
int main() {
    F[0] = 1;
    for(int i = 1; i < 110; i++) {
        F[i] = (F[i - 1] * i) % MOD;
    }

    freopen("train.in", "r", stdin);    
    freopen("train.out", "w", stdout);    
    cin >> T;
    while(T-- > 0) {
        cin >> N;
        vector<string> a;
        for(int i = 0; i < N; i++) {
            string s;
            cin >> s;
            a.push_back(s);
        }

        int ok = true;
        long long ret = 1;
        for(char ch = 'a'; ch <= 'z'; ch++) {
            vector<int> p[4];
            memset(v, 0, sizeof(v));
            for(int i = 0; i < a.size(); i++) {
                v[i] = 1;
                if (!good(a[i], ch)) ok = false;

                if (all(a[i], ch)) p[0].push_back(i);
                else if (pre(a[i], ch)) p[1].push_back(i);
                else if (suf(a[i], ch)) p[2].push_back(i);
                else if (con(a[i], ch)) p[3].push_back(i);
                else {
                    v[i] = 0;
                }
            }

            if (p[1].size() > 1) ok = false;
            if (p[2].size() > 1) ok = false;
            if (p[3].size() > 1) ok = false;
            if (p[3].size() > 0 && p[0].size() + p[1].size() + p[2].size() > 0) ok = false;

            if (!ok) break;

            if (p[0].size() + p[1].size() + p[2].size() + p[3].size() > 1) {
                stringstream ss;
                if (p[2].size() > 0) ss << a[p[2][0]];
                for(int i = 0; i < p[0].size(); i++) ss << a[p[0][i]];
                if (p[1].size() > 0) ss << a[p[1][0]];

                vector<string> set;
                set.push_back(ss.str());
                for(int i = 0; i < a.size(); i++) if (!v[i])
                    set.push_back(a[i]);
                a = set;

                ret = (ret * F[p[0].size()]) % MOD;
            }
        }
        if (ok) {
            printf("Case #%d: %lld\n", caseNumber++, (ret * F[a.size()]) % MOD);
        } else {
            printf("Case #%d: 0\n", caseNumber++);
        }
    }
    return 0;
}
