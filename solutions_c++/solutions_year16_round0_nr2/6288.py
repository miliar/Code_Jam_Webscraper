#include<bits/stdc++.h>
main()
{
	int T,t,i,is_happy,count_flip,k;
	char s[105];
    scanf("%d",&T);
    freopen("B.txt","w",stdout);
    for(t=1;t<=T;t++)
    {
    	scanf("%s",s);
    	count_flip=0;
    	k=1;
    	if(s[0]=='-')
    		is_happy=0;
    	else
    		is_happy=1;
    	for(i=1;s[i]!='\0';i++)
    	{
    		if(s[i]=='-')
    		{
    			if(is_happy)
    			{
    				k=2;
    				is_happy=0;
				}
    			
			}
    		else if(!is_happy)
    		{
    			count_flip+=k;
    			is_happy=1;
				k=1;
			}
			//printf("%d\n",count_flip);
		}
		if(!is_happy)
    		count_flip+=k;
		printf("Case #%d: %d\n",t,count_flip);
	}
    scanf(" ");
}

