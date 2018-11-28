#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<queue>
#include<set>
#include<sstream>
#include<complex>
using namespace std;
string s;
int k;
void getinput() {
    cin >> s;
    cin >> k;
}
void process() {
    int count = 0;
    for(int i = 0; i < s.size() - k + 1; i ++) {
        if (s[i] == '+') continue;
        count ++;
        for(int j = i; j < i + k; j ++) {
            if (s[j] == '-') s[j] = '+';
            else s[j] = '-';
        }
//        for(int j = 0; j < s.size(); j ++) cout << s[j]; cout << endl;
    }
    bool possible = true;
    for(int i = 0; i < s.size(); i ++)
        if (s[i] != '+') possible = false;
    if (possible) cout << count << endl;
    else cout << "IMPOSSIBLE" << endl;
}
int main() {
//    freopen("D:\\Projects\\GGCodeJam\\bai2.inp", "r", stdin);
//    freopen("D:\\Projects\\GGCodeJam\\bai2.out", "w", stdout);
    int t; cin >> t;
    for(int test = 0; test < t; test ++) {
        getinput();
        cout << "Case #" << test + 1 << ": ";
        process();
    }
    return 0;
}
