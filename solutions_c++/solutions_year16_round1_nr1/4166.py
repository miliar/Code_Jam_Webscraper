#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int  temp,i,t,c=1,count,j,pos;
	char ch;
	FILE *in,*out;
	in=fopen("test2.in","rt");
	out=fopen("rest.in","wt");
	fscanf(in,"%lld",&t);
	while(c<=t)
	{
		char string[1005];
		fscanf(in,"%s",string);
		ch=string[0];
		i=1;
		while(string[i]!='\0')
		{
			if(string[i]>=ch)
			{
				pos=i;
				temp=string[pos];
				for(j=pos-1;j>=0;j--)
					string[j+1]=string[j];
				
			
				string[0]=temp;
			}
			
			ch=string[0];
			i++;
		}
		
		fprintf(out,"Case #%d: %s\n",c,string);
		c++;
	}
	fclose(in);
	fclose(out);
	return 0;
}

