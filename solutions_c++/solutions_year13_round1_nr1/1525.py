#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main()
{
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    int T,r,t;
    scanf("%d",&T);
    for(int k=1;k<=T;k++)
    {
        scanf("%d%d",&r,&t);
        int n;
        n=((1-2*r)+sqrt((2*r-1)*(2*r-1)+8*t))/4.0;
        printf("Case #%d: %d\n",k,n);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
