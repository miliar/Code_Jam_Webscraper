#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *ftp;
	ftp=fopen("A.txt","w");
	int T,i;
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		char a[2100],j;
		int b[26]={0};
		scanf("%s",&a);
		fprintf(ftp,"Case #%d: ",i+1);
		for(j=0;a[j]!='\0';j++)
		{
			b[a[j]-65]++;
		}
		//printf("%d\n",b[0]);
		for(j=0;j<b[25];j++)
		fprintf(ftp,"0");
		b[4]-=b[25];
		b[17]-=b[25];
		b[14]-=b[25];//0
		
		b[18]-=b[23];
		b[8]-=b[23];//6
		
		b[4]=(b[4]-2*b[18]);
		b[21]-=b[18];
		b[13]-=b[18];//7
		
		b[5]-=b[21];
		b[8]-=b[21];
		b[4]-=b[21];//5
		
		b[14]-=b[5];
		b[20]-=b[5];
		b[17]-=b[5];//4
		
		b[4]=(b[4]-2*b[17]);
		b[7]-=b[17];
		b[19]-=b[17];//3
		
		b[19]-=b[22];
		b[14]-=b[22];//2
		
		b[13]-=b[14];
		
		for(j=0;j<b[14];j++)
		fprintf(ftp,"1");
		for(j=0;j<b[22];j++)
		fprintf(ftp,"2");
		for(j=0;j<b[17];j++)
		fprintf(ftp,"3");
		for(j=0;j<b[5];j++)
		fprintf(ftp,"4");
		for(j=0;j<b[21];j++)
		fprintf(ftp,"5");
		for(j=0;j<b[23];j++)
		fprintf(ftp,"6");
		for(j=0;j<b[18];j++)
		fprintf(ftp,"7");
		for(j=0;j<b[6];j++)
		fprintf(ftp,"8");
		for(j=0;j<b[13]/2;j++)
		fprintf(ftp,"9");
		fprintf(ftp,"\n");
	}
	fclose(ftp);
}
