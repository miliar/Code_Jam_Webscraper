#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

void solve() {
    int smax;
    string s;
    
    cin >> smax >> s;
    
    int cnt = s[0] - '0';
    int add = 0;
    
    for (int i = 1; i <= smax; i++) {
        if (cnt < i) {
            add += i - cnt;
            cnt = i;
        }
        cnt += s[i] - '0';
    }
    
    cout << add;
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("A-small-attempt0.in.txt", "rt", stdin);
//    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    
}
