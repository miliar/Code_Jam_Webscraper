#include<stdio.h>
int ise(int arr[10])
{
	int d=1;
	for(int i=0;i<10;i++)
	{
		if(arr[i]==0)
		{
			d=0;
			break;
		}
	}
	return d;
}
int main()
{
	int arr[10],t;
	int n;
	FILE *fp1,*fp2;
	fp1=fopen("C:\\Users\\Sh\\Desktop\\A-large.in","r");
	fp2=fopen("C:\\Users\\Sh\\Desktop\\output.txt","w");
	fscanf(fp1,"%d\n",&t);
	for(int a=0;a<t;a++)
	{
	
	for(int i=0;i<10;i++)
	{
		arr[i]=0;
	}
	fscanf(fp1,"%d\n",&n);
	if(n==0)
	fprintf(fp2,"Case #%d: INSOMNIA\n",a+1);
	else
	{
		int q=n;
	 	while(q)
	 	{
	 		arr[q%10]=1;
	 		q/=10;
		 }
     int m=n;
	 while(ise(arr)==0)
	 {
	 	n+=m;
	 	int q=n;
	 	while(q)
	 	{
	 		arr[q%10]=1;
	 		q/=10;
		 }
	 }
	 fprintf(fp2,"Case #%d: %d\n",a+1,n);
	}
}
}
