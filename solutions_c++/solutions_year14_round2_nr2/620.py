#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <stack>

#define N 10

using namespace std;
int main(){
    int nc;
    scanf("%d", &nc);
    for(int caso = 1; caso <= nc; caso++){
        int a, b, k;
        scanf("%d %d %d", &a, &b, &k);
        int ct = 0;
        for(int i = 0; i < a; i++){
            for(int j = 0; j < b; j++){
                if( (i & j) < k ) ct++;
            }
        }
        printf("Case #%d: %d\n", caso, ct);
    }
}
