#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>




int main()
{
	
	int t=0,n=0,i=0,j=0,count=0;
	char s[100],s1[20],s2[20],s3[20];
	double ans=0,C,F,X,current=2,rate,check=0;

	FILE *fin,*fout;
	fout=fopen("out.txt","w");

	fin=fopen("1.txt","r");

	fgets(s,100,fin);	

	t=atoi(s);
	

	while(n<t)
	{
		
		fgets(s,100,fin);
		sscanf(s,"%s%s%s",s1,s2,s3);
		
		
		
		C=atof(s1);
		F=atof(s2);
		X=atof(s3);

		
		while(1)
		{
			check=X/current;

			rate=(C/current)+(X/(current+F));

			if(check<rate)
			{
				ans=ans+check;
				break;
			}
			else
				ans=ans+(C/current);

			current=current+F;

		}
		
		n++;
		fprintf(fout,"Case #%d: %.7lf\n",n,ans);
		
		i=j=0;

	    ans=0,current=2,rate=check=0;
		
	}

	fclose(fout);
	fclose(fin);

	return 0;
}