#include<stdio.h>
#include<string.h>

int a[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};

char s1[10000];
char s[10000];
int getnum(char s)
{
	if(s=='i')
	{
		return 2; 
	}
	if(s=='j')
	{
       return 3;
	}
	if(s=='k')
	{
		return 4;
	}
	
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int sign=1;
    int num=0;
    int len=0;
    int len1=0;
    int i=0,j=0;
    int next=0;
    int flag=0;
    scanf("%d",&num);
    for(j=0;j<num;j++)
    {
    	
    	scanf("%d %d",&len,&len1);
    	scanf("%s",&s);
    	sign=1;
   	    next=0;
   	    flag=0;
    	
    	memset(s1,0,sizeof(s1));
    	
    	for(i=0;i<len1*len;i++)
   	    {
   	    	
    	    s1[i]=s[i%len];
    	}
    	    next=getnum(s1[0]);
        for(i=1;i<len1*len;i++)
        {
            if(a[next-1][getnum(s1[i])-1]*sign<0)
			{
			    
					
			    	next=-a[next-1][getnum(s1[i])-1]*sign;
			    		if(sign>0)
			    	{
			    		sign=sign*(-1);
			    	}
			}
			else
			{
				 
					next=a[next-1][getnum(s1[i])-1]*sign;
					  if(sign<0)
				   {
				   	  sign=sign*(-1);
				   }
			}
       	   
        }
        next=sign*next;
    	if(next!=-1)
    	{
    		printf("Case #%d: NO\n",j+1);
    	}
    	else
    	{  
           sign=1;
           next=1;
   		   for(i=0;i<len1*len;i++)
   		   {
   		   	    if(flag==2)
   		   	    {
   		   	    	break;
   		   	    }
   		   		if(a[next-1][getnum(s1[i])-1]*sign==2)
   		   		{
   		   			if(flag==0) flag++;
   		   			
   		   		}
   		   		if(a[next-1][getnum(s1[i])-1]*sign==4)
   		   		{
   		   			if(flag==1) flag++;
   		   		}
   		   	    if(a[next-1][getnum(s1[i])-1]*sign<0)
				{
			        
			    	next=-a[next-1][getnum(s1[i])-1]*sign;
					if(sign>0)
			    	{
			    		sign=sign*(-1);
			    	}
				}
				else
				{
					next=a[next-1][getnum(s1[i])-1]*sign;
					if(sign<0)
			    	{
			    		sign=sign*(-1);
			    	}
				}
			    
   		   	  
   		   }
   		   if(flag==2)
   		   {
   		   	printf("Case #%d: YES\n",j+1);
   		   }
   		   else
   		   {
   		   	printf("Case #%d: NO\n",j+1);
   		   }
   		   
    	}
    }
	
	
	return 0;
}