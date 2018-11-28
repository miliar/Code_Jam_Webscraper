#include<stdio.h>

int main(int argc,char *argv[])
{
	FILE *fp=fopen(argv[1],"r");
	char buff[1005];
	long int i=0,j=1,sum=0,diff=0,N;
	fscanf(fp,"%d",&N);
	fscanf(fp,"%d %s",&N,buff);
	while(!feof(fp))
	{
		sum=buff[0]-0x30;
		for(i=1;i<=N;i++)
		{ 
		   	if(sum>=i)
		   	   sum+=(buff[i]-0x30);
		   	else if(sum<i)
			   {
			   	  diff+=(i-sum);
			   	  sum+=(i-sum)+(buff[i]-0x30);
			   }   
		}
		printf("Case #%d: %d\n",j,diff);
		j++;
		buff[0]='\0';
		fscanf(fp,"%d %s",&N,buff);
		sum=diff=0;
	}
	
}
