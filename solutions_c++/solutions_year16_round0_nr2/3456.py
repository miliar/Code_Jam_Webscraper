//
//  main.cpp
//  codejam
//
//  Created by Todor Lyubomirov Bonchev on 1/1/16.
//

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

char state[128];
char init[128];

bool notOk() {
    for (int i = 0; i < strlen(state); ++i) {
        if (state[i]=='-') return true;
    }
    return false;
}

char tmpS[128];
void flip(int idx) {
    for (int i=idx,j=0;i>=0;--i,j++) {
        tmpS[j] = init[i]=='-'?'+':'-';
    }
    for (int i=0;i<=idx;++i) {
        init[i]=tmpS[i];
    }
}

char REZ[1000];
char* solve() {
    cin>>state;
    int len = (int)strlen(state);
    for (int i=0;i<len;++i) init[i]='+';
    int res = 0;
    for (int j=len-1;j>=0;--j) {
        if (init[j]!=state[j]) {
            res++;
            flip(j);
        }
    }
    sprintf(REZ, "%d", res);
    return REZ;
}

int main(int argc, const char * argv[]) {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int tests;
    scanf("%d\n", &tests);
    for (int test=1;test<=tests;++test) {
        printf("Case #%d: %s\n", test, solve());
    }

    return 0;
}
