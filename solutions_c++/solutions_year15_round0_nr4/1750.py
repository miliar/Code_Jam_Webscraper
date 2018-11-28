#include <iostream>
#include <cstdio>

using namespace std;

int T;
int X, R, C;

int main()
{
    freopen("D-small-attempt5.in", "r", stdin);
    freopen("D-small-attempt5.out", "w", stdout);

    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%d %d %d", &X, &R, &C);

        bool OK = true;
        if( R*C%X ) OK = false;

        if( R > C ) swap(R, C);
        if( X >= R*2+1 ) OK = false;
        if( X >= C+1 ) OK = false;
        if( X == 4 && R == 2 && C == 4 ) OK = false;

        printf("Case #%d: ", Ti);

        if( !OK ) puts("RICHARD");
        else puts("GABRIEL");
    }
}
