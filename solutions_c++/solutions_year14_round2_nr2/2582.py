#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int getbitand(int, int);

int main()
{
    int test;
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    scanf("%d", &test);
    int a, b, k;
    int dec, cnt = 0;
    for(int i = 1; i <= test; i++){
            //printf("test: %d\n", i);
            scanf("%d", &a);
            scanf("%d", &b);
            scanf("%d", &k);
            for(int i = 0; i < a; i++){
                for(int j = 0; j < b; j++){
                    dec = getbitand(i, j);
                    //printf("%d\n", dec);
                    if(dec < k){
                        cnt++;
                    }
                }
            }
            printf("Case #%d: %d\n", i, cnt);
            cnt = 0;
    }
    return 0;
}

int getbitand(int i, int j){
    return (i & j);
}
