#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int l,t,n,i,j,k;
	FILE *ptr,*ptr1;
	char s[109];
	ptr=fopen("B-large.in","r+");
	ptr1=fopen("B-large2.in","w+");
	fscanf(ptr,"%lld",&t);
	for(j=1;j<=t;j++)
	{
		fscanf(ptr,"%s",&s);
		long long int f=0;
		long long int c=0;
		for(i=strlen(s)-1;i>=0;i--)
		{
			if(f==0&&s[i]=='-')
			{
				f=1;
				c+=1;
			}
			else if(f==1&&s[i]=='+')
			{
				f=0;
				c+=1;
			}
		}
		fprintf(ptr1,"Case #%lld: %lld\n",j,c);
	}
	fclose(ptr);
	fclose(ptr1);
	return 0;
}
