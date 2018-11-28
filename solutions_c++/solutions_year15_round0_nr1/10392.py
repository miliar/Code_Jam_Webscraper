#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t;
	FILE *f1=fopen("input.in","r");
	FILE *f2=fopen("output_1.txt","w");
	fscanf(f1,"%d",&t);
	for(int j=1;j<=t;j++)
	{
		int s_max;
		char shyness[1005];
		fscanf(f1,"%d %s",&s_max,shyness);
		//cout<<shyness<<endl;
		int curr_count=0;
		int answer=0;
		for(int i=0;i<s_max+1;i++)
		{
			if(curr_count>=i&&(shyness[i]-'0')>0)
			{
				curr_count+=shyness[i]-'0';
			}
			else if(curr_count<i&&(shyness[i]-'0')>0)
			{
				answer+=i-curr_count;
				curr_count+=shyness[i]-'0'+answer;
			}
		
		}
		fprintf(f2,"Case #%d: %d\n",j,answer);
		//cout<<"Case #"<<j<<": "<<answer<<endl;
	}
	return 0;
}
