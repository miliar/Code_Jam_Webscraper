#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int  i,testcases,check,ans;
	FILE *input,*output;
	char s[105];
	input=fopen("super.in","rt");
	output=fopen("man.in","wt");
	fscanf(input,"%lld",&testcases);
	for(check=1;check<=testcases;)
	{
		
		ans=0;
			
		fscanf(input,"%s",s);
		for(i=1;s[i]!='\0';)
		{
			if(s[i-1]!=s[i])
			{
				ans++;
			}
			i++;	
		}
		if(s[i-1]=='-')
			ans++;
		
		fprintf(output,"Case #%d: %lld\n",check,ans);
		check++;
	}
	fclose(input);
	fclose(output);
	return 0;
}

