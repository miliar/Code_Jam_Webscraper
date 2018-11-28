#include<stdio.h>

int main()
{
	int t,ar[4][4],val[17],i,j,num1,num2,num0,cases;
	scanf("%d",&t);
	for(cases=1;cases<=t;cases++)
	{
	 num0=num1=num2=0;
	 for(i=0;i<17;i++)
	 val[i]=0;
	 
	 scanf("%d",&num0);
	 for(i=0;i<4;i++)
	 for(j=0;j<4;j++)
	 scanf("%d",&ar[i][j]);
	 
	 num0--;
	 
	 for(j=0;j<4;j++)
	 val[ar[num0][j]]++;	
	 
	 scanf("%d",&num0);
	 for(i=0;i<4;i++)
	 for(j=0;j<4;j++)
	 scanf("%d",&ar[i][j]);
	 
	 num0--;
	 
	 for(j=0;j<4;j++)
	 val[ar[num0][j]]++;
	 
	 num0=num1=num2=0;
	 for(i=1;i<=16;i++)
	 {
	 	if(val[i]==0)num0++;
	 	if(val[i]==1)num1++;
	 	if(val[i]==2)num2++;
	 }
	 
	 if(num2==0)
	 printf("Case #%d: Volunteer cheated!\n",cases);
	 
	 else if(num2>1)
	 printf("Case #%d: Bad magician!\n",cases);
	 
	 else
	 {
	 	for(i=1;i<=16;i++)
	 	if(val[i]==2)
	 	{
	 		printf("Case #%d: %d\n",cases,i);
	 		break;
	 	}
	 }
	}
	

	
	return 0;
}
