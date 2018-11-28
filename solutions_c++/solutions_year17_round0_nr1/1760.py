//
// Created by Denis Mukhametianov on 08.04.17.
//

#include <cstdio>
#include <iostream>
#include <string>
#include <vector>


using namespace std;


void solve(int testNumber) {
    string s;
    int k;
    cin >> s >> k;
    int answer = 0;
    for(int i = 0; i < s.length() - k + 1; i++) {
        if(s[i] == '-') {
            answer++;
            for(int j = 0; j < k; j++)
                s[i + j] = ('+' + '-') - s[i + j];
        }
    }
    for(int i = 0; i < s.length(); i++)
        if(s[i] == '-')
            answer = -1;
    if(answer == -1)
        printf("Case #%d: IMPOSSIBLE\n", testNumber);
    else
        printf("Case #%d: %d\n", testNumber, answer);
}


void runA() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int tc;
    cin >> tc;
    for(int i = 0; i < tc; i++)
        solve(i + 1);
}