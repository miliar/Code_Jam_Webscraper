#include <string>
#include <string.h>
#include <stdio.h>
#include <iostream>
using namespace std;

int main() {
    int t;
    scanf("%d",&t);
    for (int ii = 1; ii <= t; ii++) {
        

        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);
        long long base = 1;
        for (int i = 0; i < c; i++)
            base *= k;
        long long bb = base / k;
        int flag = 0;
        // vector<long long> v;
        printf("Case #%d:", ii);
        for (long long i = 1; i <= base; i += bb) {
            printf(" %lld", i);
        }
        printf("\n");
    }
}