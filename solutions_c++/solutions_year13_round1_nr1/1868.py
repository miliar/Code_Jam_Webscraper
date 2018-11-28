// Google Code Jam Round 1A Problem A
#include <cstdio>
#include <iostream>
using namespace std;

int tc;

int main() {
    freopen("a_input.txt", "r", stdin);
    freopen("a_output.txt", "w", stdout);
    scanf("%d", &tc);
    for ( int i = 0; i < tc; i++ ) {
        int r, t;
        scanf("%d%d", &r, &t);
        int cnt = r+1;
        for (;t>=0;cnt+=2) t -= cnt*cnt-(cnt-1)*(cnt-1);
        printf("Case #%d: %d\n", i+1, (cnt-r-2)/2);
    }
    //system("PAUSE");
    return 0;
}
