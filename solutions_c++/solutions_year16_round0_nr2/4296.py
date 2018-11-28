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
char s[111];
int cases = 0;

int main() {
    scanf("%d",&T);
    while( T-- ) {
        scanf("%s",s);
        int len = strlen(s);
        int cnt = 0;
        for(int i = len - 1; i >= 0 ; i-- ) {
            int nSide;
            if( s[i] == '-' ) {
                nSide = 0;
            } else {
                nSide = 1;
            }
            
            if( cnt & 1 ) {
                nSide = 1-nSide;
            }
            if( nSide == 0 ) {
                cnt++;
            }
        }
        printf("Case #%d: %d\n",++cases,cnt);
    }
    return 0;
}