#include <iostream>
#include <cstdio>
using namespace std;

int a, t;
int main()
{
    scanf("%d", &t);
    while(t--)
    {
        a++;
        int x, r, c, g=0;
        scanf("%d%d%d", &x, &r, &c);
        if(x==1)
            g=1;
        else if(x==2)
        {
            if((r*c)%2==0)
                g=1;
        }
        else if(x==3)
        {
            if(!((r*c)%3!=0||r*c==3))
                g=1;
        }
        else
        {
            if(r*c==12||r*c==16)
                g=1;
        }
        printf("Case #%d: ", a);
        printf(g==1 ? "GABRIEL\n" : "RICHARD\n");
    }
    return 0;
}
