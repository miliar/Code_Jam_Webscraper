#include<stdio.h>
int main()
{
	 int a[101];
	int n,i,count=0,j,temp,temp1,temp2;
	FILE *fp,*fp1;
	fp1=fopen("output3.txt","wt");
	fp=fopen("A-large.in","rt");
	while(!feof(fp))
	{
		fscanf(fp,"%d",&a[count]);
		
		count++;
	}
	for(i=0;i<a[0];i++)
	{
		int b[10]={0};
		n=a[i+1];
		if(n==0)
		fprintf(fp1,"case #%d: INSOMNIA\n",i+1);
		else
		{
			j=1;
			count=0;
			while(count!=10)
			{
				temp1=n*j;
				temp2=temp1;
				while(temp1!=0)
				{
					temp=temp1%10;
					if(b[temp]==0)
					{
						b[temp]=1;
						count++;
					}
					temp1=temp1/10;
				}
				j++;
			}
			fprintf(fp1,"case #%d: %d\n",i+1,temp2);
		}
	}
	fclose(fp1);
	return 0;
}
