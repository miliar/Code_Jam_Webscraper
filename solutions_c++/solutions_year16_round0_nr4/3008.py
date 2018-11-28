/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Alex
 *
 * Created on 2016年4月10日, 上午 6:39
 */

#include <cstdlib>
#include <cstdio>

using namespace std;

/*
 * 
 */
void Solve() {
    int total;
    scanf("%d", &total);
    
    for(int i = 0; i < total; i++) {
        int K, C, S;
        scanf("%d %d %d", &K, &C, &S);
        printf("Case #%d: ", i+1);
        for(int j = 1; j <= K; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }

    return;
}

int main(int argc, char** argv) {
    Solve();

    return 0;
}

