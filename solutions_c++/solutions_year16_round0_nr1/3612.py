/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Alex
 *
 * Created on 2016年4月9日, 下午 3:54
 */

#include <cstdlib>
#include <string>
#include <unordered_set>

using namespace std;

/*
 * 
 */

void findDigit(unordered_set<int>& digitSet, unsigned long long N) {
    while(N > 0) {
        digitSet.insert(N%10);
        N/=10;
    }

    return;
}

void Solve() {
    int total;
    scanf("%d", &total);

    for(int i = 0; i < total; i++) {
        unsigned long long N;
        unordered_set<int> digitSet; 
        scanf("%llu", &N);
        printf("Case #%d: ", i+1);

        if(N == 0) {
            printf("INSOMNIA\n");
        }
        else {
            unsigned long long j;
            for(j = 1; digitSet.size() < 10; j++) {
                findDigit(digitSet, j * N);
            }
            printf("%llu\n", (j - 1) * N);
        }
    }

    return;
}

int main(int argc, char** argv) {
    Solve();

    return 0;
}

