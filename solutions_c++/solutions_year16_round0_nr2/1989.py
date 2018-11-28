#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <random>
#include <iostream>
#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
#endif

using namespace std;
typedef pair<int, int> ii;


int nTest;
char s[111];

int main(){
#ifndef ONLINE_JUDGE
    freopen("b.inp", "r", stdin);
    freopen("b.out", "w", stdout);
#endif

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        scanf("%s\n", s);
        int len = strlen(s);
        s[len] = '+';
        s[len + 1] = '\0';
        len ++;
        int cnt = 0;
        for (int i = 1; i < len; i++){
            if (s[i] != s[i - 1]) cnt++;
        }
        printf("%d\n", cnt);
    }
    

    return 0;
}