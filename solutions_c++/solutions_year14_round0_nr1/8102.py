#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main()
{
int T=0,I=0;
int row1[4],row2[4];
int junk[4];
int ans1=0,ans2=0;

int Tcount=1;

scanf("%d\n",&T);
	for(Tcount=1;Tcount<=T;Tcount++)
	{
		ans1=0;ans2=0;
		for(I=0;I<4;I++)
		{
			row1[I]=0;
			row2[I]=0;
		}
		scanf("%d\n",&ans1);
		//printf("%d\n",ans1);
		for(I=0;I<(ans1-1);I++)
		{
			scanf("%d %d %d %d\n",&junk[1],&junk[2],&junk[3],&junk[0]);
		}
		scanf("%d %d %d %d\n",&row1[0],&row1[1],&row1[2],&row1[3]);
		for(I=ans1;I<4;I++)
		{
			scanf("%d %d %d %d\n",&junk[1],&junk[2],&junk[3],&junk[0]);
		}
	
	
		//printf("%d %d %d %d\n",row1[0],row1[1],row1[2],row1[3]);
		
		scanf("%d\n",&ans2);
		//printf("%d\n",ans2);
		for(I=0;I<(ans2-1);I++)
		{
			scanf("%d %d %d %d\n",&junk[1],&junk[2],&junk[3],&junk[0]);
		}
		scanf("%d %d %d %d\n",&row2[0],&row2[1],&row2[2],&row2[3]);
		for(I=ans2;I<4;I++)
		{
			scanf("%d %d %d %d\n",&junk[1],&junk[2],&junk[3],&junk[0]);
		}
	
	
		//printf("%d %d %d %d\n",row2[0],row2[1],row2[2],row2[3]);

	int flag=0,J=0;
	int temp=0;
	for(I=0;I<4;I++)
	{
		for(J=0;J<4;J++)
		{
		if(row1[I]==row2[J])
		{flag++;temp=row1[I];}
		}
	}
		
	if(flag==0)
	printf("Case #%d: Volunteer cheated!\n",Tcount);
	else if(flag==1)
	printf("Case #%d: %d\n",Tcount,temp);
	else if(flag>1)
	printf("Case #%d: Bad magician!\n",Tcount);
	}		

return 0;
}
