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
char s[1111];

int main(){
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        scanf("%s\n", s);
        vector<char>pre, suf;
        pre.clear();
        suf.clear();
        pre.push_back(s[0]);
        int n = strlen(s);
        for (int i = 1; i < n; i++){
        	if (s[i] >= pre.back()) pre.push_back(s[i]);
        	else suf.push_back(s[i]);
        }
        while (!pre.empty()){
        	printf("%c", pre.back());
        	pre.pop_back();
        }
        for (int i = 0; i < suf.size(); i++) printf("%c", suf[i]);
        printf("\n");
    }
    

    return 0;
}