#include<stdio.h>
int main()
{
    long test;
    scanf("%ld",&test);
    long p=1;
    while(p<=test)
    {
        long x,y,z;
        scanf("%ld",&x);
        scanf("%ld",&y);
        scanf("%ld",&z);
        long pp=1;
        printf("Case #%ld: ",p);
        while(pp<=z)
        {
            printf("%ld ",pp);
            pp++;
        }
        printf("\n");
        p++;
    }
    return 0;
}