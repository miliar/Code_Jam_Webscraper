#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <fstream>

using namespace std;


int main(){
    freopen ("A-large.in", "r", stdin);
    freopen ("A-large.out", "w", stdout);
    int T;
    int i, j, k, t;
    int s;
    char v[1000+5];
    scanf("%d", &T);
    for( t = 1; t <= T; t++){
        scanf("%d", &s);
        scanf("%s", v);
        int cur = 0;
        int res = 0;
        for( i = 0; i <= s; i ++){
            if( cur < i && v[i] != '0' ){
                res += (i - cur);
                cur += (i - cur);
            }
            cur += v[i] - '0';
        }
        printf("Case #%d: %d\n", t, res);
    }
    return 0;
}
