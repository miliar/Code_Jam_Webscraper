#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{	//author : rocknik
	//nikunjj46@gmail.om
	int t;
	FILE *fp1=fopen("infile.in","r");
	FILE *fp2=fopen("outputfile.txt","w");
	fscanf(fp1,"%d",&t);
	for(int j=1;j<=t;j++)
	{
		int s_max;
		char shy[1005];
		fscanf(fp1,"%d %s",&s_max,shy);
		//cout<<shyness<<endl;
		int count=0;
		int res=0;
		for(int i=0;i<s_max+1;i++)
		{
			if(count>=i&&(shy[i]-'0')>0)
			{
				count+=shy[i]-'0';
			}
			else if(count<i&&(shy[i]-'0')>0)
			{
				res+=i-count;
				count+=shy[i]-'0'+res;
			}
		
		}
		fprintf(fp2,"Case #%d: %d\n",j,res);
		//cout<<"Case #"<<j<<": "<<answer<<endl;
	}
	return 0;
}
