#include<stdio.h>


int main()
{
	
	int i,j,k,a[4][4],b[4][4],count,r,h;
	scanf("%d",&i);
	
	while(i!=0)
	{
		scanf("%d",&j);
		for(int l=0;l<4;l++)
		{
			for(int m=0;m<4;m++)
			{
				scanf("%d",&a[l][m]);
			}
		}
		
		scanf("%d",&k);
		for(int l=0;l<4;l++)
		{
			for(int m=0;m<4;m++)
			{
				scanf("%d",&b[l][m]);
			}
		}
		count=0;
		
		for(int l=0;l<4;l++)
		{
			for(int m=0;m<4;m++)
			{
				if(a[j-1][l]==b[k-1][m])
				{
					count++;
					r=j-1,h=l;
				}
			}
		}
		
		switch(count)
		{
			case 0:
				printf("Volunteer cheated!\n");
				break;
				case 1:
					printf("%d\n",a[r][h]);
					break;
					default:
						printf("Bad magician!\n");
			
		}
	}
	
	
	return 0;
}
