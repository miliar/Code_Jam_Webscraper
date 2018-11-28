#include<stdio.h>
#include<math.h>
int main()
{
	 int i,r,t,j,c,m;
	//char a[5][5],junk;
	freopen("in7.in","r",stdin);
	freopen("test_out.txt","w",stdout);
	
	scanf("%d",&m);
	//printf("%d\n",m);
	for(i=1;i<=m;i++)
	{   c=0;	
		scanf("%d %d",&r,&t);
		//	printf("%d %d\n",r,t);
	
			j=pow(r+1,2)-pow(r,2);
			while(j<=t)
			{
				c++;
				t=t-j;
				j=j+4;	
			}
		
					printf("Case #%d: %d\n",i,c);			
		
	}							
		//printf("%d\n",w);
	
	return 0;
}
