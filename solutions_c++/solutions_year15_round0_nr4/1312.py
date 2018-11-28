#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
using namespace std;
bool malt[5][5][5];
int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("Dout.out", "w", stdout);
    int x, r, c;
    int t;
    scanf("%d", &t);
    int numCase = 1;
    while(t--)
    {
        scanf("%d%d%d", &x, &r, &c);
        bool flag;
        if(x == 1)
        {
            flag = true;
        }
        else if(x == 2)
        {
            if((r * c) % x == 0) flag = true;
            else
                flag = false;
        }
        else if(x == 3)
        {
            if(r * c == 6 || (r >= 3 && c >= 3))
            {
                if(c == 4 && r == 4) flag = false;
                else
                    flag = true;
            }
            else
                flag = false;
        }
        else
        {
            if(r * c == 12 || r * c == 16) flag = true;
            else
                flag = false;
        }
        if(flag) printf("Case #%d: GABRIEL\n", numCase++);
        else
            printf("Case #%d: RICHARD\n", numCase++);
    }
    return 0;
}
