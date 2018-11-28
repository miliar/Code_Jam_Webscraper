#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *input;
	FILE *output;
	input=fopen("anku.in","r");
	output=fopen("fun546.in","w");
	long long int testcases;
	long long int count,number;
	fscanf(input,"%lld",&testcases);
	for(count=1;count<=testcases;)
	{
		fscanf(input,"%lld",&number);
		long long int temp=number;
		int visit[10];
		int  i,c=-1,d;
		long long int temp2;
		long long int answer,j=2;
		for(i=0;i<10;i++)
			visit[i]=0;
			
		if(number==0)
		fprintf(output,"Case #%lld: INSOMNIA\n",count);
		else
		{
		for(;1;)
		{
			temp2=number;
			while(number!=0)
				{
					d=number%10;
					number=number/10;
					if(visit[d]==0)
					{
						visit[d]=1;
						c++;
					}
					if(c==9)
					{
						answer=temp2;
						break;
					}
				}
				if(c==9)
					break;
				number=temp*j;
				j++;
			}
			fprintf(output,"Case #%lld: %lld\n",count,answer);
		}
		count++;
	}
	fclose(input);
	fclose(output);
	return 0;
}
