#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <cmath>
#include <queue>
#include <set>
#include <functional>
using namespace std;

int T;
int N;
int ss = (1<<10) - 1;
int cases = 0;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    while( T-- ) {
        printf("Case #%d: ",++cases);
        scanf("%d",&N);
        if( N == 0 ) {
            printf("INSOMNIA\n");
            continue;
        }
        int t = 0;
        int last = 0;
        while( t!= ss ) {
            last += N;
            int tt = last;
            while( tt ) {
                int modn = tt % 10;
                t = t|(1<<modn);
                tt /= 10;
            }
        }
        printf("%d\n",last);
    }
    return 0;
}