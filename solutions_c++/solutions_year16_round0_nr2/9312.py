    #include<stdio.h>
    #include<string.h>
    #include<stdlib.h>
    int main()
    {
    	int T,len,c=0,i,j,k;
    	char str[1000];
    	scanf("%d",&T);
    	k=1;
    	while(T--)
    	{
    		c=0;
    		scanf("%s",str);
    		len=strlen(str);
    		for(i=len-1;i>=0;i--)
    		{
    			if(str[i]=='-')
    			{
    				for(j=0;j<=i;j++)
    				{
    					if(str[j]=='+')
    					str[j]='-';
    					else if(str[j]=='-')
    					str[j]='+';
    				}
    					c++;
    			}
    		}
    		printf("Case #%d: %d\n",k,c);
    		k++;
    	}
    	return 0;
    }


