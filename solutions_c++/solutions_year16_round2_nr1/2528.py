#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main()
{
	//freopen("result.txt","w",stdout);
	int cas;
	scanf("%d ",&cas);
	for(int t=0;t<cas;t++)
	{
		char c[2200];
		gets(c);
		int counts[10]={0},alp[26]={0};
		int length=strlen(c);
		for(int i=0;i<length;i++)
		{
			alp[c[i]-'A']++;
			if(c[i]=='Z' && alp['Z'-'A']!=0)
			{
				counts[0]++;
				alp['Z'-'A']--;
				alp['E'-'A']--;
				alp['R'-'A']--;
				alp['O'-'A']--;
			}
			else if(c[i]=='W' && alp['W'-'A']!=0)
			{
				counts[2]++;
				alp['T'-'A']--;
				alp['W'-'A']--;
				alp['O'-'A']--;
			}
			else if(c[i]=='X' && alp['X'-'A']!=0)
			{
				counts[6]++;
				alp['S'-'A']--;
				alp['I'-'A']--;
				alp['X'-'A']--;
			}
			else if(c[i]=='G' && alp['G'-'A']!=0)
			{
				counts[8]++;
				alp['E'-'A']--;
				alp['I'-'A']--;
				alp['G'-'A']--;
				alp['H'-'A']--;
				alp['T'-'A']--;
			}
		}
		while(alp['S'-'A']>0)
		{
			counts[7]++;
			alp['S'-'A']--;
			alp['E'-'A']--;
			alp['V'-'A']--;
			alp['E'-'A']--;
			alp['N'-'A']--;
		}
		while(alp['V'-'A']!=0)
		{
			counts[5]++;
			alp['F'-'A']--;
			alp['I'-'A']--;
			alp['V'-'A']--;
			alp['E'-'A']--;
		}
		while(alp['F'-'A']!=0)
		{
			counts[4]++;
			alp['F'-'A']--;
			alp['O'-'A']--;
			alp['U'-'A']--;
			alp['R'-'A']--;
		}
		while(alp['O'-'A']!=0)
		{
			counts[1]++;
			alp['O'-'A']--;
			alp['N'-'A']--;
			alp['E'-'A']--;
		}
		while(alp['T'-'A']!=0)
		{
			counts[3]++;
			alp['T'-'A']--;
			alp['H'-'A']--;
			alp['R'-'A']--;
			alp['E'-'A']--;
			alp['E'-'A']--;
		}
		while(alp['I'-'A']!=0)
		{
			counts[9]++;
			alp['N'-'A']--;
			alp['I'-'A']--;
			alp['N'-'A']--;
			alp['E'-'A']--;
		}
		printf("Case #%d: ",t+1);
		for(int i=0;i<10;i++)
			for(int j=0;j<counts[i];j++)
				printf("%d",i);
		printf("\n");
	}
}
