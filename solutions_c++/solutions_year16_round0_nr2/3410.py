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
        char s[101];
        scanf("%s",&s);
        int n=0;
        char c=s[0];
        for(int i=0;s[i]!='\0';i++)
        {
            if(s[i]!=c)
            {
                n++;
                c=s[i];
            }
        }
        if(c=='-')
            n++;
        printf("Case #%i: %i\n",x,n);
        x++;
    }
	return 0;
}
