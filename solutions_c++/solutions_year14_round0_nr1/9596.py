/*google code jam */


#include <stdio.h>
int c[17];
int main(void) {
  
  int l,t,n1,n2,ans,i,j,k,tmp,f;
  scanf("%d",&t);
  
  // t test cases
  
  for(l=1;l<=t;l++)
  {
  	for(k=1;k<17;k++)
    {
    	c[k]=0;
  	 }
  	 f=0;
  
  	scanf("%d",&n1);
  	for(i=1;i<=4;i++)
  	{
  		for(j=1;j<=4;j++)
  		{
  			scanf("%d",&tmp);
  			if(i==n1)
  			c[tmp]++;
  		}
  	}
  	scanf("%d",&n2);
  	for(i=1;i<=4;i++)
  	{
  		for(j=1;j<=4;j++)
  		{
  			scanf("%d",&tmp);
  			if(i==n2)
  			c[tmp]++;
  		}
  	}
  	
    for(k=1;k<17;k++)
  {	if(c[k]==2)
  	{
  		ans=k;
  		f++;
     }
  }
  	if(f==1)
  	printf("Case #%d: %d\n",l,ans);
  	if(f==0)
	printf("Case #%d: Volunteer cheated!\n",l);
  	if(f>1)
	printf("Case #%d: Bad magician!\n",l);
  	
   }

	return 0;
}
