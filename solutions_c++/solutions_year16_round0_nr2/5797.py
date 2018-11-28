#include <stdio.h>
int main()
{
	int T,i=1,k,flip;
	char s[101];
	scanf("%d",&T);
    while(i<=T)
    {
    	k=0;
    	flip=0;
    	scanf("%s",s);
        while(s[k+1]!='\0')
		{
			if(s[k]!=s[k+1])
			flip++;
			k++;
		}
		if(s[k]=='-')
		flip++;
		printf("case #%d: %d\n",i,flip);
		i++;
	}
	return 0;
}

