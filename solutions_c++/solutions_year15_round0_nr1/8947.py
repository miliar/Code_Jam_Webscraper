#include<stdio.h>
#include<string.h>
int main()
{
	long long int n,t,i,j,k;
	//scanf("%lld",&t);
	
	//freopen ("myfile.txt","r",stdin);
	FILE *fp1;
	fp1 = fopen("myfile.txt","r+");
	fscanf(fp1,"%lld",&t);
	//if(myfile.isopen())
	//{
		
	//}
	FILE *fp;

   fp = fopen("test.txt", "w+");
	for(k=1;k<=t;k++)
	{
		fscanf(fp1,"%lld",&n);
		char c[n+5];
		fscanf(fp1,"%s",c);
		j=0;
		long long int a,b=0;
		for(i=0;i<strlen(c);i++)
		{
			if(b<i)
			{
			//b=i;
			j=j+i-b;
			b=i;
			}
			a=c[i]-48;
			b=b+a;
			//if(c[i]=='0')
			//j++;
		}
		fprintf(fp,"Case #%lld: %lld\n",k,j);
	}
	fclose (fp);  
	fclose (fp1);  
	return 0;
}
