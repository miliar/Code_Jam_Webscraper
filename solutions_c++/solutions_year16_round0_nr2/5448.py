#include<bits/stdc++.h>
using namespace std;
int main()
{
	typedef long long lld;
	FILE *input,*output;
	lld t,count,count1,i,j,m;
	char str[1000],str2[1000],ch1;
	input=fopen("input.txt","r");
	if(input==NULL)
	{
		printf("ERROR!!");
		exit(0);	
	}
	output=fopen("output.txt","w");
	if(output==NULL)
	{
		printf("Error!!");
		exit(0);
	}
	fscanf(input,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(input,"%s",str);
		ch1=str[0];
		count=1;
		for(j=1;j<strlen(str);j++)
		{
			if(str[j]==ch1)
			{
				continue;
			}
			else
			{
				count++;
				ch1=str[j];
			}
		}
		//cout<<count<<" "<<endl;
		cout<<count<<str[strlen(str)-1]<<endl;
		if(str[strlen(str)-1]=='+')
		{
			fprintf(output,"Case #%lld: %lld\n",i,count-1);
		}
		else
		{
			fprintf(output,"Case #%lld: %lld\n",i,count);
		}	
	}
	return 0;
}
