#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,cs=0,i,n;
	char str[3000],c;
	scanf("%d",&t);
	while(t--)
	{
		cs++;
		int al[26] = {0},dig[10] = {0};

		scanf("%s",str);
		n = strlen(str);
		for(i=0;i<n;i++)
		{
			c = str[i];
			//zero
			if(c=='Z')
			{
				al['E'-'A']--;
				al['R'-'A']--;
				al['O'-'A']--;
				dig[0]++;
			}
			//two
			else if(c=='W')
			{
				al['T'-'A']--;
				al['O'-'A']--;
				dig[2]++;
			}
			//four
			else if(c=='U')
			{
				al['F'-'A']--;
				al['O'-'A']--;
				al['R'-'A']--;
				dig[4]++;
			}
			//six
			else if(c=='X')
			{
				al['S'-'A']--;
				al['I'-'A']--;
				dig[6]++;
			}
			//eight
			else if(c=='G')
			{
				al['E'-'A']--;
				al['I'-'A']--;
				al['H'-'A']--;
				al['T'-'A']--;
				dig[8]++;
			}
			else
			{
				al[c-'A']++;
			}

		}
		//one
		while(al['O' - 'A']--)
		{
			al['N'-'A']--;
			al['E'-'A']--;
			dig[1]++;
		}
		//three
		while(al['R' - 'A']--)
		{
			al['T'-'A']--;
			al['H'-'A']--;
			al['E'-'A']-=2;
			dig[3]++;
		}
		//five
		while(al['F' - 'A']--)
		{
			al['I'-'A']--;
			al['V'-'A']--;
			al['E'-'A']--;
			dig[5]++;
		}
		//seven
		while(al['S' - 'A']--)
		{
			al['V'-'A']--;
			al['N'-'A']--;
			al['E'-'A']-=2;
			dig[7]++;
		}
		//nine
		while(al['I' - 'A']--)
		{
			al['E'-'A']--;
			al['N'-'A']-=2;
			dig[9]++;
		}
		printf("Case #%d: ",cs);
		for(i=0;i<10;i++)
		{
			if(dig[i]!=0)
			{
				while(dig[i]--)
					printf("%d",i);
			}
		}
		printf("\n");


	}
}