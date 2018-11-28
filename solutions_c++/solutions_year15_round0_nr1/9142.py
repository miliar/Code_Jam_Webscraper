#include<stdio.h>
#include<stdlib.h>


int main()
{
	FILE *fin,*fout;
	int t,n,i=0,j=0,count,X=1;
	char str[2000];
	//scanf("%d",&t);

	fin=fopen("input.txt","r");
	fout=fopen("out.txt","w");

	fgets(str,2000,fin);
	t=atoi(str);
	while(t--)
	{
		
		char s[1005],c,p[10];
		int num=0,temp;

		fgets(str,2000,fin);
		sscanf(str,"%s%s",p,s);

		n=atoi(p);

		count=0;
		//scanf("%d %s",&n,s);

		for(i=0;i<=n;i++)
		{
			j=s[i]-'0';
			
			if(count<i && j!=0)
			{
				temp=(i-count);
				num=num+temp;
				count=count+temp;
			}
			count+=j;
		}

		//printf("Case #%d: %d\n",X,num);
		fprintf(fout,"Case #%d: %d\n",X,num);
	
		X++;
		
	}
	fclose(fin);
	fclose(fout);
	return 0;
}