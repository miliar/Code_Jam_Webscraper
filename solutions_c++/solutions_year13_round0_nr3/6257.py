#include <stdio.h>
#include <math.h>
#include <string.h>

typedef unsigned short int _int;

char isPalin(long long c)
{
	char num[102], x, y, z;
	
	sprintf(num, "%lld", c);
	x = strlen(num) - 1;
	z = x/2;
	
	for(y = 0; y <= z; y++)
		if(num[y] != num[x - y])
			break;
	
	return y > z;	//palindrome
}

int main()
{
    _int x, t;
    unsigned long c, a, b, y, z, cnt = 0;
    long long sqr, palin[100000];

    freopen("A-small.in", "r", stdin);
    freopen("outf.txt", "w", stdout);

    if(stdin == 0 || stdout == 0)
    {
    	printf("No file\n");
        return -1;
    }

    scanf("%d", &t);
    
    for(c = 1; c <= 10000000; c++)
    {
    	if(isPalin(c))
		{
			sqr = c*c;
			if(isPalin(sqr))
	    		palin[cnt++] = sqr;
		}
/*    	{
    		sqr = (long long)c*c;
   			
    		for(pos = 0; pos < cnt; pos++)
    		{
    			diff = palin[pos] - root;
    			if(diff > 0)
    				break;
   				else if(diff == 0)
   				{
					palin[cnt++] = c;
					break;
   				}
    		}
    	}
*/    }
    
    for(x = 0; x < t; x++)
    {
    	scanf("%d %d", &a, &b);
    	
    	for(y = 0; palin[y] < a; y++);
   		
   		z = 0;
   		while(palin[y] <= b)
   		{
   			y++;
   			z++;
   		}
    	
        printf("Case #%d: %d\n", x + 1, z);
    }
    return 0;
}
