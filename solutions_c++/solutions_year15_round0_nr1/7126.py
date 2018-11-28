/* 
 * File:   main.cpp
 * Author: escortkeel
 *
 * Created on 11 April 2015, 12:33 PM
 */

#include <cstdio>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        int N, ans = 0;
        scanf(" %d ", &N);
        int data[1002];
        
        for(int j = 0; j <= N; j++) {
            char c;
            scanf("%c", &c);
            data[j]= c - '0';
        }
        int p =0;
        for(int j =0; j <= N; j++) {
            if(j > p) {ans++;p++;}
            p+= data[j];
        }
        
        printf("Case #%d: %d\n", i + 1, ans);
    }

    return 0;
}

