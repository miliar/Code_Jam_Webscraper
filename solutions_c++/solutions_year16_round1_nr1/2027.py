#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("output-large.txt", "w", stdout);
    string s;
    int t;
    scanf("%d", &t);
    for(int j = 1; j <= t; j++) {
        cin >> s;
        string s1 = "";
        s1 = s[0];
        int len = s.length();
        for(int i = 1; i < len; i++) {
            if(s[i] >= s1[0])
                s1 = s[i] + s1;
            else
                s1 = s1+s[i];
        }
        cout << "Case #" << j << ": " << s1 << "\n";

    }

    return 0;
}

//g++ lastword.cpp -std=c++11 -o lastword