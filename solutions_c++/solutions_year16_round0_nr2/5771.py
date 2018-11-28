#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int z,n,a,b,c;
    char t[105];

	scanf ("%d", &z);

	for (a=1; a<=z; a++)
    {
        printf ("Case #%d: ", a);

        scanf ("%s", t);

        c=1;

        for (b=0; t[c]; b++)
        {
            for (; t[c] && t[c]==t[c-1]; c++);

            if (!t[c])
                break;

            c++;
        }

        if (t[c-1]=='-')
            b++;

        printf ("%d\n", b);
    }

	return 0;
}
