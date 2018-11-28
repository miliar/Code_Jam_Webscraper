#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{
	FILE* in=fopen("input.in","r");
	FILE* out=fopen("output.txt","w");
	int t,s;
	char a[1000];
	fscanf(in,"%d",&t);
	for(int j=1;j<=t;j++)
	{
		int ans=0,temp=0;		
		fscanf(in,"%d",&s);	
		fgetc(in);	
	fgets(a,s+2,in);
	temp=a[0]-'0';
	for(int i=1;i<s+1;i++)
		{			
			//fprintf(out," #%d: %d\n",i,a[i]-'0');
			if(a[i]!='0')
		    if(temp<i)
		    {
				 ans=ans+i-temp;
		         temp=a[i]-'0'+i;				
		    }
			else
				temp=temp+a[i]-'0';
		}
		fprintf(out,"Case #%d: %d\n",j,ans);
	}
}