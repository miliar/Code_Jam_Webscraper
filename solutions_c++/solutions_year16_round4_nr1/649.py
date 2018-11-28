#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>

using namespace std;

string gen(int n, char win) {
    if (n == 0) {
        string ans = "";
        ans += win;
        return ans;
    }
    string q1 = gen(n - 1, win);
    string q2;
    if (win == 'P') {
        q2 = gen(n - 1, 'R');
    } else 
    if (win == 'R') {
        q2 = gen(n - 1, 'S');
    } else {
        q2 = gen(n - 1, 'P');
    }
    
    return min(q1 + q2, q2 + q1);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testCases;
    cin >> testCases;
    for (int testCase = 1; testCase <= testCases; testCase++) {
        cout << "Case #" << testCase << ": ";
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        
        string ans = "Z";       
        int rr, pp, ss;
        string temp = gen(n, 'R');
        rr = pp = ss = 0;
        for (int i = 0; i < temp.size(); i++) {
            if (temp[i] == 'R') {
                rr++;
            }
            if (temp[i] == 'S') {
                ss++;
            }
            if (temp[i] == 'P') {
                pp++;
            }
        }    
        if (rr == r && pp == p && ss == s) {
            ans = min(ans, temp);
        }       
        temp = gen(n, 'P');
        rr = pp = ss = 0;
        for (int i = 0; i < temp.size(); i++) {
            if (temp[i] == 'R') {
                rr++;
            }
            if (temp[i] == 'S') {
                ss++;
            }
            if (temp[i] == 'P') {
                pp++;
            }
        }    
        if (rr == r && pp == p && ss == s) {
            ans = min(ans, temp);
        }        
        temp = gen(n, 'S');
        rr = pp = ss = 0;
        for (int i = 0; i < temp.size(); i++) {
            if (temp[i] == 'R') {
                rr++;
            }
            if (temp[i] == 'S') {
                ss++;
            }
            if (temp[i] == 'P') {
                pp++;
            }
        }    
        if (rr == r && pp == p && ss == s) {
            ans = min(ans, temp);
        }               
        
        if (ans == "Z") {
            ans = "IMPOSSIBLE";
        }
        
        cout << ans << endl;
    } 
    return 0;
}