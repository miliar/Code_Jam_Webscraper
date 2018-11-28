#include <stdio.h>
#include <string.h>

int main()
{
	int T;
	int smax;
	char s[2000];
    scanf("%d",&T);
    int answer = 0;
    int laps = 0;
    for (int ts=0;ts<T;ts++)
    {
    	scanf("%d %s",&smax,s);
    	answer = 0;
    	laps = s[0] - '0';
    	for (int i=1;i<=smax;i++)
    	{
    		if (laps>=i)
    		{
    			laps+= s[i] - '0';
    		}
    		else
    		{
    			answer+= i-laps;
    			laps = i;
    			laps+= s[i] - '0';
    		}
    	}
    	printf("Case #%d: %d\n",ts+1,answer);
    }
	return 0;
}