#include<stdio.h>
#include<string.h>
#include<math.h>

struct input
{
	char a[3],b[3];

};

input in[16];

int main()
{
	
	int t=0,n=0,i=0,j=0,r1=0,r2=0,check=0,count=0,token,len,no;
	char s[100],s1[3],s2[3],s3[3],s4[3],ans[3];

	FILE *fin,*fout;
	fout=fopen("out.txt","w");

	fin=fopen("1.txt","r");

	fgets(s,100,fin);	

	len=strlen(s);

	while(s[i]!=10)
	{
		no=s[i]-'0';
		no=no*pow(10.0,(len-i-2));
		t=t+no;

		i++;
	}
	
	
	

	while(n<t)
	{
		fgets(s,100,fin);	


		len=strlen(s);
		i=0;
		while(s[i]!=10)
		{
			no=s[i]-'0';
			no=no*pow(10.0,(len-i-2));
			r1=r1+no;
			i++;
		}
		//scanf("%d",&r1);
		
		

		for(j=0;j<16;j=j+4)
		{
			fgets(s,100,fin);
			sscanf(s,"%s%s%s%s",in[j].a,in[j+1].a,in[j+2].a,in[j+3].a);
		}
		
		fgets(s,100,fin);

		len=strlen(s);
		i=0;
		while(s[i]!=10)
		{
			no=s[i]-'0';
			no=no*pow(10.0,(len-i-2));
			r2=r2+no;
			i++;
		}
		//scanf("%d",&r1);
		
		

		
		for(j=0;j<16;j=j+4)
		{
			fgets(s,100,fin);
			sscanf(s,"%s%s%s%s",in[j].b,in[j+1].b,in[j+2].b,in[j+3].b);
		}
		
		i=0;
		
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			if(strcmp(in[4*(r1-1)+i].a,in[4*(r2-1)+j].b)==0)
			{
				strcpy(ans,in[4*(r1-1)+i].a);
				count++;
			}
			
			
		}
	

		

		n++;
		if(count==1)
		{
			fprintf(fout,"Case #%d: %s\n",n,ans);
			
		}
		else if(count==0)
		{
			fprintf(fout,"Case #%d: Volunteer cheated!\n",n);
		}
		else
			fprintf(fout,"Case #%d: Bad magician!\n",n);
	
		
		i=j=r1=r2=count=len=no=0;

	}

	fclose(fout);
	fclose(fin);

	return 0;
}