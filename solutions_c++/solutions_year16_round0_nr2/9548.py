#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,j=1;
	FILE *f11,*f22;
	f11=fopen("B-large (1).in","r");
	f22=fopen("a3.in","w");
	fscanf(f11,"%d",&t);
	while(t--)
	{
		char str[105];
		fscanf(f11,"%s",str);
		int count1=0;
		int i=1;
		while(str[i]!='\0')
		{
			if(str[i-1]!=str[i])
			count1++;
			i++;
		}
		if(str[i-1]=='-')
			count1++;

		fprintf(f22,"Case #%d: %lld\n",j,count1);
		j++;
	}
	fclose(f11);
	fclose(f22);
	return 0;
}

