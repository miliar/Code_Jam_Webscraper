#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int  i,t,c=1,count;
	FILE *in,*out;
	in=fopen("asdf.in","rt");
	out=fopen("best.in","wt");
	fscanf(in,"%lld",&t);
	while(c<=t)
	{
		char string[110];
		fscanf(in,"%s",string);
		count=0;
		i=1;	
		while(string[i]!='\0')
		{
			if(string[i-1]!=string[i])
			count++;
			i++;	
		}
		if(string[i-1]=='-')
			count++;
		
		fprintf(out,"Case #%d: %lld\n",c,count);
		c++;
	}
	fclose(in);
	fclose(out);
	return 0;
}

