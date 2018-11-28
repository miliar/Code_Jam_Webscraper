// A C program to implement Ukkonen's Suffix Tree Construction
// Here we build generalized suffix tree for two strings
// And then we find longest common substring of the two input strings
#include <stdio.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
#define MAXN 2005

ll n, m, t;

char flip(char c){
    return c == '+' ? '-' : '+';
}

int main()
{
    cin >> t;
    for (int cse = 1; cse <= t; cse++){
        string s;
        ll n;
        cin >> s >> n;
        ll cnt = 0;
        for (int i = 0; i < s.size() - n + 1; i++){
            if (s[i] == '-'){
                for (int j = 0; j < n; j++){
                    s[i+j] = flip(s[i+j]);
                }
                cnt++;
            }
        }
        for (int i = 0; i < s.size(); i++){
            if (s[i] == '-') cnt = -1;
        }
        cout << "Case #" << cse << ": ";
        if (cnt == -1){
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            cout << cnt << endl;
        }
    }
    return 0;
}

