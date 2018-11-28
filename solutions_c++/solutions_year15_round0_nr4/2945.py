#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int cases,caseno=0,x,r,c;

    scanf("%d", &cases);

    while(cases--)
    {
        scanf("%d%d%d", &x, &r, &c);

        printf("Case #%d: ", ++caseno);

        if(x==1)
            printf("GABRIEL\n");
        else if(x==2 && r%2 && c%2)
            printf("RICHARD\n");
        else if(x==2)
            printf("GABRIEL\n");
        else if(x==3 && (r==1 || c==1) )
            printf("RICHARD\n");
        else if(x==3 && (r*c)%3==0)
            printf("GABRIEL\n");
        else if(x==3)
            printf("RICHARD\n");
        else if(x==4 && r*c>=12)
            printf("GABRIEL\n");
        else
            printf("RICHARD\n");
    }

    return 0;
}
