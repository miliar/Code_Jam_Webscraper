#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <cstring>

using namespace std;

char phone[2002];
int charNum[26];
int len;
int nl[1000];

bool check(int po)
{
	//printf("po is %d\n", po);
//	for(int i=0;i<26;i++)
	//	printf("%d ", charNum[i]);
	//for(int j=0;j<po;j++)
	//	printf("%d ", nl[po]);
	//printf("\n");
	bool rv;
	int t=0;
	for(int i=0;i<26;i++)
	{
		if(charNum[i]>0)
		{
			t=1;
			break;
		}	
	}
	if(t==0)
	{
		for(int j=0;j<po;j++)
			printf("%d", nl[j]);
		printf("\n");
		return true;
	}
	
	if(charNum['Z'-'A']>=1 && charNum['E'-'A']>=1 && charNum['R'-'A']>=1 && charNum['O'-'A']>=1)
	{
		charNum['Z'-'A']-=1;
		charNum['E'-'A']-=1;
		charNum['R'-'A']-=1;
		charNum['O'-'A']-=1;
		nl[po]=0;
		//printf("Now 0 is checked\n");
		if(check(po+1))
			return true;
		charNum['Z'-'A']+=1;
		charNum['E'-'A']+=1;
		charNum['R'-'A']+=1;
		charNum['O'-'A']+=1;
	}
	if(charNum['O'-'A']>=1 && charNum['N'-'A']>=1 && charNum['E'-'A']>=1)
	{
		charNum['O'-'A']-=1;
		charNum['N'-'A']-=1;
		charNum['E'-'A']-=1;
		nl[po]=1;
		//printf("Now 1 is checked\n");
		if(rv=check(po+1))
			return true;
		charNum['O'-'A']+=1;
		charNum['N'-'A']+=1;
		charNum['E'-'A']+=1;
	}
	if(charNum['T'-'A']>=1 && charNum['W'-'A']>=1 && charNum['O'-'A']>=1)
	{
		charNum['T'-'A']-=1;
		charNum['W'-'A']-=1;
		charNum['O'-'A']-=1;
		nl[po]=2;
		//printf("Now 2 is checked\n");
		if(rv=check(po+1))
			return true;
		charNum['T'-'A']+=1;
		charNum['W'-'A']+=1;
		charNum['O'-'A']+=1;
	}
	if(charNum['T'-'A']>=1 && charNum['H'-'A']>=1 && charNum['R'-'A']>=1 && charNum['E'-'A']>=2)
	{
		charNum['T'-'A']-=1;
		charNum['H'-'A']-=1;
		charNum['R'-'A']-=1;
		charNum['E'-'A']-=2;
		nl[po]=3;
		//printf("Now 3 is checked\n");
		if(rv=check(po+1))
			return true;
		charNum['T'-'A']+=1;
		charNum['H'-'A']+=1;
		charNum['R'-'A']+=1;
		charNum['E'-'A']+=2;
	}	
	if(charNum['F'-'A']>=1 && charNum['O'-'A']>=1 && charNum['U'-'A']>=1 && charNum['R'-'A']>=1)
	{
		charNum['F'-'A']-=1;charNum['O'-'A']-=1;charNum['U'-'A']-=1;charNum['R'-'A']-=1;
		nl[po]=4;
		//printf("Now 4 is checked\n");
		if(rv=check(po+1))
			return true;
		charNum['F'-'A']+=1;charNum['O'-'A']+=1;charNum['U'-'A']+=1;charNum['R'-'A']+=1;
	}
	if(charNum['F'-'A']>=1 && charNum['I'-'A']>=1 && charNum['V'-'A']>=1 && charNum['E'-'A']>=1)
	{
		charNum['F'-'A']-=1;charNum['I'-'A']-=1;charNum['V'-'A']-=1;charNum['E'-'A']-=1;
		nl[po]=5;
		//printf("Now 5 is checked\n");
		if(rv=check(po+1))
			return true;
		charNum['F'-'A']+=1;charNum['I'-'A']+=1;charNum['V'-'A']+=1;charNum['E'-'A']+=1;
	}
	if(charNum['S'-'A']>=1 && charNum['I'-'A']>=1 && charNum['X'-'A']>=1)
	{
		charNum['S'-'A']-=1;charNum['I'-'A']-=1;charNum['X'-'A']-=1;
		nl[po]=6;
		//printf("Now 6 is checked\n");
		if(rv=check(po+1))
			return true;
		charNum['S'-'A']+=1;charNum['I'-'A']+=1;charNum['X'-'A']+=1;
	}
	if(charNum['S'-'A']>=1 && charNum['E'-'A']>=2 && charNum['V'-'A']>=1 && charNum['N'-'A']>=1)
	{
		charNum['S'-'A']-=1;charNum['E'-'A']-=2;charNum['V'-'A']-=1;charNum['N'-'A']-=1;
		nl[po]=7;
		//printf("Now 7 is checked\n");
		if(rv=check(po+1))
			return true;
		charNum['S'-'A']+=1;charNum['E'-'A']+=2;charNum['V'-'A']+=1;charNum['N'-'A']+=1;
	}
	if(charNum['E'-'A']>=1 && charNum['I'-'A']>=1 && charNum['G'-'A']>=1 && charNum['H'-'A']>=1 && charNum['T'-'A']>=1)
	{
		charNum['E'-'A']-=1;charNum['I'-'A']-=1;charNum['G'-'A']-=1;charNum['H'-'A']-=1;charNum['T'-'A']-=1;
		nl[po]=8;
		//printf("Now 8 is checked\n");
		if(rv=check(po+1))
			return true;
		charNum['E'-'A']+=1;charNum['I'-'A']+=1;charNum['G'-'A']+=1;charNum['H'-'A']+=1;charNum['T'-'A']+=1;
	}
	if(charNum['N'-'A']>=2 && charNum['I'-'A']>=1 && charNum['E'-'A']>=1)
	{
		charNum['N'-'A']-=2;charNum['I'-'A']-=1;charNum['E'-'A']-=1;
		nl[po]=9;
		//printf("Now 9 is checked\n");
		if(rv=check(po+1))
			return true;
		charNum['N'-'A']+=2;charNum['I'-'A']+=1;charNum['E'-'A']+=1;
	}
	return false;
}

int main()
{
	int test_case;
	scanf("%d", &test_case);
	for(int i=1;i<=test_case;i++)
	{
		memset(charNum, 0, 26);
		scanf("%s", phone);
		len=strlen(phone);
		for(int i=0;i<len;i++)
			charNum[phone[i]-'A']++;
		//for(int i=0;i<26;i++)
		//	printf("%d ", charNum[i]);
		//printf("\n");
		printf("Case #%d: ", i);
		check(0);
	}
	return 0;
}
