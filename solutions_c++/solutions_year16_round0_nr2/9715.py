#include<stdio.h>
#include<string.h>
int main()
{
	FILE *fp1,*fp2;
	int t;
	fp1=fopen("C:\\Users\\Sh\\Desktop\\B-large.in","r");
	fp2=fopen("C:\\Users\\Sh\\Desktop\\output.txt","w");
	fscanf(fp1,"%d\n",&t);
	char s[101],s1[100];
	
	for(int a=0;a<t;a++)
	{
	
	fscanf(fp1,"%s\n",s);
	int n=strlen(s),c=0;
	s1[c]=s[0];
	for(int i=1;i<n;i++)
	{
		if(s1[c]!=s[i])
		{
			c++;
			s1[c]=s[i];
		}
		
	}
	int sum=0;
	if(s1[0]=='-')
	sum+=1;
	for(int i=1;i<=c;i++)
	{
		if(s1[i]=='-')
		sum+=2;
	}
	fprintf(fp2,"Case #%d: %d\n",a+1,sum);
}
return 0;
}
