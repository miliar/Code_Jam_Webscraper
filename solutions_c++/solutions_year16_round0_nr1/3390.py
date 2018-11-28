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

bool hasUnseen(bool s[10]) {
    for (int i=0;i<10;++i) {
        if (s[i]==false) {
            return true;
        }
    }
    return false;
}

char numbers[512];

char* solve() {
    long long n;
    cin >> n;
    long long inp = n;
    sprintf(numbers, "%lld", n);
    bool seti[10];
    fill(seti, seti+10, false);
    for (int j=0;j<strlen(numbers);++j){
        seti[numbers[j]-'0']=1;
    }
    int i=0;
    while (hasUnseen(seti) && i<20000) {
        i++;
        n+=inp;
        sprintf(numbers, "%lld", n);
        for (int j=0;j<strlen(numbers);++j) {
            seti[numbers[j]-'0']=1;
        }
    }
    if (i == 20000) {
        return (char*)"INSOMNIA";
    }
    sprintf(numbers, "%lld", n);
    return numbers;
}

int main(int argc, const char * argv[]) {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for (int test=1;test<=tests;++test) {
        printf("Case #%d: %s\n", test, solve());
    }
    
    return 0;
}
