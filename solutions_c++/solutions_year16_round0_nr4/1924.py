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
int c, k, s;



int main(){
#ifndef ONLINE_JUDGE
    freopen("d.inp", "r", stdin);
    freopen("d.out", "w", stdout);
#endif

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        scanf("%d %d %d", &k, &c, &s);
        for (int i = 1; i <= k; i++) printf("%d ", i);
        printf("\n");
        
    }
    

    return 0;
}