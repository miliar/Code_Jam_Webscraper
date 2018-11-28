#include <stdio.h>

int main()
{
	int t;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++)
	{
		int cont[20];
		for(int i=0;i<20;i++) cont[i]=0;
		for(int j=0;j<=1;j++)
		{
			int l;
			scanf("%d",&l);
			for(int a=1;a<=4;a++)
			{
				for(int b=1;b<=4;b++)
				{
					int aux;
					scanf("%d",&aux);
					if(a==l) cont[aux]++;	
				}
			}
		}
		int r=0;
		int resp=0;
		for(int i=1;i<=16;i++) 
		{	
			//printf("%d\n",cont[i]);
			if(cont[i]==2) 
			{	
				r++;
				resp=i;
			}
		}
		printf("Case #%d: ",ti);
		if(r==0) printf("Volunteer cheated!\n");
		if(r==1) printf("%d\n",resp);
		if(r>1) printf("Bad magician!\n");
	}
	return 0;
}
