#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main()
{
    int t,x=1;
    scanf("%i",&t);
    while(t--)
    {
        int k,c,s;
        long long int po;
        scanf("%i%i%i",&k,&c,&s);
        printf("Case #%i: ",x);
        for(int i=0;i<k;i++)
        {
            printf("%i ",i+1);
        }
        printf("\n");
        x++;
    }
	return 0;
}
