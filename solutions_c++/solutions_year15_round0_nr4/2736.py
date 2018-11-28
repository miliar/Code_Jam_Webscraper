#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define disable printf("Case #%d: RICHARD\n", Case)
#define able printf("Case #%d: GABRIEL\n", Case)

int X, R, C;


int main()
{
//    freopen("in.txt", "r", stdin);
    freopen("D-small-attempt3.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; Case++)
    {
        scanf("%d%d%d", &X, &R, &C);
        if(R * C % X != 0)
            disable;
        else if(R * C == X && X <= 2)
            able;
        else if(R * C == X && X > 2)
            disable;
        else if(X != 4)
            able;
        else if(R * C >= 12)
            able;
        else
            disable;
    }
    return 0;
}
