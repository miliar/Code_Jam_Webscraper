#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	long long z,n,a,b,c,d;
	char s[17];
    long long t[11];
    long long x,y;

	a=0;
	printf("Case #1:\n");
    b=1;

    for (c=1; c<16; c++)
        b*=2;

    b++;

	for (; a<50; b+=2)
    {
        for (c=2; c<=10; c++)
            t[c]=0;

        for (c=2; c<=10; c++)
        {
            x=0;
            y=1;

            for (d=b; d; d/=2)
            {
                if (d%2)
                    x+=y;

                y*=c;
            }

            y=2;

            if (x%y)
                for (y=3; y<x && y<=1000; y+=2)
                    if (x%y==0)
                        break;

            if (y<x && x%y==0)
                t[c]=y;
            else
                break;
        }

        if (c==11)
        {
            a++;
            c=0;

            for (d=b; d; d/=2)
                s[c++]=d%2+'0';

            reverse(s,s+c);

            s[c]=0;
            printf ("%s", s);

            for (c=2; c<=10; c++)
                printf(" %lld", t[c]);

            printf ("\n");
        }
    }

	return 0;
}
