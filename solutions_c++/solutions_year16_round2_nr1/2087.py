#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int T;

void fill(char* str, int* charCounts)
{
	for(int i = 0; i < 2048; i++)
	{
		charCounts[i] = 0;
	}
	int len = strlen(str);
	for(int i = 0; i < len; i++)
	{
		charCounts[str[i]]++; 
	}
}

char* process(int* charCounts)
{
	char* resultStr = new char[2048];
	for(int i = 0; i < 2048; i++)
	{
		resultStr[i] = 0;
	}
	int phoneNumCounts[10];
	for(int i = 0; i < 10; i++)
	{
		phoneNumCounts[i] = 0;
	}
	while(charCounts['Z'])
	{
		charCounts['Z']--;
		charCounts['E']--;
		charCounts['R']--;
		charCounts['O']--;
		phoneNumCounts[0]++;
	}
	while(charCounts['W'])
	{
		charCounts['T']--;
		charCounts['W']--;
		charCounts['O']--;
		phoneNumCounts[2]++;
	}
	while(charCounts['U'])
	{
		charCounts['F']--;
		charCounts['O']--;
		charCounts['U']--;
		charCounts['R']--;
		phoneNumCounts[4]++;
	}
	while(charCounts['X'])
	{
		charCounts['S']--;
		charCounts['I']--;
		charCounts['X']--;
		phoneNumCounts[6]++;
	}
	while(charCounts['G'])
	{
		charCounts['E']--;
		charCounts['I']--;
		charCounts['G']--;
		charCounts['H']--;
		charCounts['T']--;
		phoneNumCounts[8]++;
	}
	while(charCounts['O'])
	{
		charCounts['O']--;
		charCounts['N']--;
		charCounts['E']--;
		phoneNumCounts[1]++;
	}	
	while(charCounts['H'])
	{
		charCounts['T']--;
		charCounts['H']--;
		charCounts['R']--;
		charCounts['E']--;
		charCounts['E']--;
		phoneNumCounts[3]++;
	}
	while(charCounts['F'])
	{
		charCounts['F']--;
		charCounts['I']--;
		charCounts['V']--;
		charCounts['E']--;
		phoneNumCounts[5]++;
	}
	while(charCounts['S'])
	{
		charCounts['S']--;
		charCounts['E']--;
		charCounts['V']--;
		charCounts['E']--;
		charCounts['N']--;
		phoneNumCounts[7]++;
	}
	while(charCounts['E'])
	{
		charCounts['N']--;
		charCounts['I']--;
		charCounts['N']--;
		charCounts['E']--;
		phoneNumCounts[9]++;
	}
	
	int resultNextIndex = 0;
	for (int i = 0; i < 10; i++)
	{
		while(phoneNumCounts[i])
		{
			resultStr[resultNextIndex++] = '0' + i;
			phoneNumCounts[i] --;
		}
	}

	return resultStr;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		char str[2048];
		int charCounts[2048];

		scanf("%s", str);
		
		fill(str, charCounts);
		char* resultstr = process(charCounts);
		printf("Case #%d: %s\n", i, resultstr);
	}

	return 0;
}