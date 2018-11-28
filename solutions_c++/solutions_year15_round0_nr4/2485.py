#include <stdio.h>
#include <string>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++)
    {
        int x, r, c;
        scanf("%d%d%d", &x, &r, &c);
        string winner = "GABRIEL";
        if ((r * c) % x != 0)
        {
            winner = "RICHARD";
        }
        if (x == 3)
        {
            if (r == 1 || c == 1)
            {
                winner = "RICHARD";
            }
        }
        if (x == 4)
        {
            if (r == 1 || c == 1)
            {
                winner = "RICHARD";
            }
            if (r == 2 && (c == 2 || c == 4))
            {
                winner = "RICHARD";
            }
            if (r == 4 && c == 2)
            {
                winner = "RICHARD";
            }
        }
        printf("Case #%d: %s\n", cases, winner.c_str());
    }
    return 0;
}
