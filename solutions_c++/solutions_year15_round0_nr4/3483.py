#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
using namespace std;
const int MAX_N = 110;
int TC, S, len;
#define INF 9999999
int main()
{
    int T, X, R, C;
    bool ans;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &TC);
    for(T = 1; T <= TC; T++ ) {
        printf("Case #%d: ",T);
        scanf("%d %d %d", &X, &R, &C);
        ans = false;
        switch(X) {
        case 1:
            ans = true;
            break;
        case 2:
            if(R%2==0 || C%2==0)
                ans = true;
            break;
        case 3:
            if(R%3==0 && C!=1)
                ans = true;
            if(C%3==0 && R!=1)
                ans = true;
            break;
        case 4:
            if(R==4 && (C==3 || C==4))
                ans = true;
            if(C==4 && (R==3 || R==4))
                ans = true;
            break;
        default:
            break;
        }
        if(ans)
            printf("GABRIEL\n");
        else
            printf("RICHARD\n");
    }
    return 0;
}

