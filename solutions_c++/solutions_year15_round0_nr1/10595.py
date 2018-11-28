#include <stdio.h>
#include <string.h>
int main(void) {
	long int t,j;
	scanf("%d",&t);
	j=t;
	while(t--)
	{
	    int n=0;
	    scanf("%d",&n);
	    char s[100];
	    gets(s);int flag=0;int r=0;
	    int i=0;int sum=0;
	    
	    for(i=1;i<=n+1;i++)
	    {
	        int a=s[i];
	        int b=a-'0';
	        if(b==0)
	            flag=1;
	        else
	        {
	            if(flag==1)
	            {
	                int g;
	                
	                g=(i-1)-sum;
	                if(g>0)
	                r+=g;
	                sum+=r;
	                
	                flag=0;
	            }
	            
	        }
	        
	        sum+=b;
	        
	    }
	    if(r>=0)
	    printf("Case #%d: %d\n",(j-t),r);
	    
	}
	return 0;
}


