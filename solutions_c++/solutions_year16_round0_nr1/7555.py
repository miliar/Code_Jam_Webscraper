#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int makearr(long long int arr[],long long int num)
{
	int flag=0,i;
	//printf("i am here\n %d",num);
	while(num>0)
	{
		arr[num%10]++;
		num=num/10;
	}
	for(i=0;i<10;i++)
	{
		if(arr[i]==0)
		{
			flag=1;
			break;
		}
	}
	if(flag==0)
	{
		return 1;
	}
	else 
		return 0;
	
	
}
int main()
{
	FILE *fp;
	fp=fopen("output.txt","w");
	long long int test,k,i,num,onum,flag,count;
	FILE *fp1=fopen("input.txt","r");
	long long int arr[10]={0};
	fscanf(fp1,"%lld",&test);
	long long int loop=1;
	while(loop<=test)
	{
		
		for(i=0;i<10;i++)
		{
			arr[i]=0;
		}
		fscanf(fp1,"%lld",&num);
		onum=num;
		if(num==0)
		{
			fprintf(fp,"Case #%d: INSOMNIA\n",loop);
		}
		else if(num==1)
		{
			fprintf(fp,"Case #%d: 10\n",loop);
		}
		else if(num==2)
		{
			fprintf(fp,"Case #%d: 90\n",loop);
		}
		else
		{
			k=2;
			flag=0;
			while(flag==0)
			{
				int ans=makearr(arr,num);
				if(ans==1)
				{
					flag=num;
					break;
				}
				else
				{
					num=onum*k;
					k=k+1;
				}
			}
			fprintf(fp,"Case #%d: %d\n",loop,flag);
		}
		loop++;
	}
	fclose(fp1);
	fclose(fp);
}
