#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,j=1;
	FILE *f1,*f2;
	f1=fopen("abcl.in","r");
	f2=fopen("a1.in","w");
	fscanf(f1,"%d",&t);
	while(t--)
	{
		char s[105];
		fscanf(f1,"%s",s);
		int count=0;
		int i=1;	
		while(s[i]!='\0')
		{
			if(s[i-1]!=s[i])
			count++;
			i++;	
		}
		if(s[i-1]=='-')
			count++;
		
		fprintf(f2,"Case #%d: %lld\n",j,count);
		j++;
	}
	fclose(f1);
	fclose(f2);
	return 0;
}

