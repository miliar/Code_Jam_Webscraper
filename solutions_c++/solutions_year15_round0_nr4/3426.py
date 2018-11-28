#include <iostream>

using namespace std;

int X, R, C;

bool fun()
{
    if (X == 1) 
        return true;
    if (X == 3)
    {
        if (R % 2 == 0 && C == 3) return true;
        if (R == 3 && C % 2 == 0) return true;
        if (R == 3 && C == 3) return true;
        return false;
    }
    if (X == 2)
    {
        if (R % 2 == 0 || C % 2 == 0) 
            return true;
        return false;
    }
    if (X == 4)
    {
        if (R == 3 && C == 4) return true;
        if (R == 4 && C == 4) return true;
        if (R == 4 && C == 3) return true;
        return false;
    }
    return false;
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int c = 1; c <= T; c++)
    {
        printf("Case #%d: ", c);
        scanf("%d%d%d", &X, &R, &C);
        if (fun() == true)
            printf("GABRIEL\n");
        else
            printf("RICHARD\n");
    }
}