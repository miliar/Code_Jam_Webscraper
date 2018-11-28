#include<iostream>
#include<cstdio>
#include<set>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>

using namespace std;

int main() {
    int t,a,b,k,i,j,count;
    scanf("%d", &t);
    for(int x=1; x<=t; x++) {
        count = 0;
        scanf("%d %d %d", &a, &b, &k);
        for(i=0; i<a; i++) {
            for(j=0; j<b; j++) {
//                printf("i&j: %d\n", i&j);
                if((i&j) < k) {
                    //printf("i: %d, j: %d\n", i, j);
                    count++;
                }
            }
        }
        printf("Case #%d: %d\n", x, count);
    }
    return 0;
}
