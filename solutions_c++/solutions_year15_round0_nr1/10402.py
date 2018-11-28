#include <stdio.h>
int main() {
	int t,i,s,add,sum,diff,cs,num,d[101];
	char c[101];
	scanf("%d",&t); cs=0;
	while(t--)
	{   add=0; sum=0; cs++;
	    scanf("\n%d ",&s);
        for(i=0;i<=s;i++)	    
        {
            scanf("%c",&c[i]);
            d[i]=c[i]-48; 
            if(i>0 && d[i]!=0)
            {
                if(sum<i)
                {
                    diff=i-sum;
                    add+=diff;
                    sum+=add; 
                }
                
            }
            sum+=d[i];
        }
        printf("Case #%d: %d\n",cs,add); 
	}
	return 0;
}