#include <stdio.h>

#include <algorithm>
using namespace std;

char pan[1000];
int main() {
    int t, n, cnt;
    scanf("%d", &t);
    fgets(pan, 1000, stdin);
    for (int c=1; c<=t; c++) {
        memset(pan, 0, sizeof(pan));
        fgets(pan, 1000, stdin);
        cnt = 0;
        for (n=0; pan[n]; n++)
            pan[n] = (pan[n]=='+' ? 0 : 1); 
        pan[n-1] = 0;
        for (int i=0; i<n-1; i++)
            if (pan[i]!=pan[i+1]) cnt++;
        if (pan[n-1]) cnt++;
        printf("Case #%d: %d\n", c, cnt);
    }
}


