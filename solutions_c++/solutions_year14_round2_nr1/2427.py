#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main() {
	// your code goes here
	char str1[104],str2[105],n,c=1;
	int i,j,l1,l2,flag,t;
	FILE *fp1,*fp2;
	fp1=fopen("akhi1.in","r");
	fp2=fopen("out.txt","w");
	fscanf(fp1,"%d",&t);
	
	while(t--)
	{
		
		fscanf(fp1,"%d",&n);
		fscanf(fp1,"%s",str1);
		l1=strlen(str1);
		fscanf(fp1,"%s",str2);
		l2=strlen(str2);
		i=j=flag=1;
		//printf("%d\n",flag);
		int count=0;
		if(str1[0]!=str2[0])
		flag=0;
		while((i<l1 || j<l2) && flag==1)
		{
			if(str1[i]!=str2[j])
			{
				if(str1[i]==str1[i-1])
			i++,count++;
			else if(str2[j]==str2[j-1])
			j++,count++;
			else
			flag=0;
			}
			else
			{
				i++;
				j++;
			}
		}
		if(flag==1)
		fprintf(fp2,"Case #%d: %d\n",c,count);
		else
		fprintf(fp2,"Case #%d: Fegla Won\n",c);
		//printf("%d\n",t);
		c++;
	}
	return 0;
}
