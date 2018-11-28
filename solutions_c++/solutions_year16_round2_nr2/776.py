#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int C, J;

bool fit (string s, int x){
    for (int i = s.length()-1; i >= 0; i--){
        if (s[i] != '?' && s[i] != char(x%10 + '0')) return false;
        x /= 10;
    }
    if (x > 0) return false;
    return true;
}

void update(int x, int y){
    if (C == -1) C = x, J = y;
    else{
        if (abs(x-y) < abs(C-J) || (abs(x-y) == abs(C-J) && x < C) || (abs(x-y) == abs(C-J) && x == C && y < J)) C = x, J = y;
    }
}

void solve (){
    C = J = -1;
    string s, t;
    cin >> s >> t;
    for (int i = 0; i < 1000; i++)
        for (int j = 0; j < 1000; j++)
            if (fit(s,i) && fit(t,j)) update(i,j);
    if (s.length() == 1) cout << C << " " << J << endl;
    if (s.length() == 2) printf("%02d %02d\n", C, J);
    if (s.length() == 3) printf("%03d %03d\n", C, J);
}

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ": ";
        solve();
    }
    return 0;
}
