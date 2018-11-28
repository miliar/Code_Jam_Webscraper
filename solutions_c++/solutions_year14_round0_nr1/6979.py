#include<stdio.h>
int main()
{
 int t,r1,r2,i,j,k,val;
 int row1[4];
 int row2[4];
 scanf("%d",&t);
 for(k=1;k<=t;k++)
  {
    scanf("%d",&r1);
    for(i=1;i<=4;i++)
    {
	if(i == r1)
	{
	  for(j=0;j<4;j++)
	   {
		scanf("%d",&row1[j]);  
	   }
	}
	else
	{
	   for(j=0;j<4;j++)
	   {
		scanf("%d",&val);
	   }		
	}
    }

    scanf("%d",&r2);
    for(i=1;i<=4;i++)
    {
	if(i == r2)
	{
	  for(j=0;j<4;j++)
	   {
		scanf("%d",&row2[j]);  
	   }
	}
	else
	{
	  for(j=0;j<4;j++)
	   {
		scanf("%d",&val);
	   }			
	}
    }

    int matches = 0;
    int matched = -1;
    for(i=0;i<4;i++)
     {
	for(j=0;j<4;j++)
	{
	  if(row1[i] == row2[j])
	   {
		matched = row1[i];
		matches++;
		break; //at most 1 match
	   }	
	}
     }
  
    if(matches == 1)
	{
		printf("Case #%d: %d\n",k,matched);
	}    				
    else if(matches > 1)
	{
		printf("Case #%d: Bad magician!\n",k);
	}
    else if(matches == 0)
	{
		printf("Case #%d: Volunteer cheated!\n",k);
	} 		
  }	
}
