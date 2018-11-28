#include <bits/stdc++.h>

using namespace std;

char s[1001];

int main()
{
	int t1;
	FILE *ftr;
	FILE *ftr1;
	ftr=fopen("input.in","r");
	ftr1=fopen("output.txt","w");
	fscanf(ftr,"%d",&t1);

	for(int t=1;t<=t1;t++)
	{
		int n;
		fscanf(ftr,"%d",&n);

		fscanf(ftr,"%s",s);
		int l1=strlen(s);

		int answer=0;

		int counter=(s[0]-'0');

		for(int i=1;i<l1;i++)
		{
			if(counter<i)
			{
				answer=answer+i-counter;
				counter=i;
			}
			counter=counter+(s[i]-'0');
		}

		fprintf(ftr1,"Case #%d: %d\n",t,answer);
	}
return 0;}