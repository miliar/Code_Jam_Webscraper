#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int z,n,a,b,c;
	bool t[10];

	scanf ("%d", &z);

	for (a=1; a<=z; a++)
    {
        printf ("Case #%d: ", a);

        for (b=0; b<10; b++)
            t[b]=0;

        scanf ("%d", &n);

        if (n==0)
        {
            printf ("INSOMNIA\n");
            continue;
        }

        c=n;

        while (1)
        {
            for (b=c; b; b/=10)
                t[b%10]=1;

            for (b=0; b<10 && t[b]; b++);

            if (b==10)
                break;

            c+=n;
        }

        printf ("%d\n", c);
    }

	return 0;
}
