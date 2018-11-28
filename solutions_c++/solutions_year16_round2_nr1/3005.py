#include<iostream>
#include<map>
#include<algorithm>
#include<vector>
#include<queue>
#include<stdio.h>
#include<string.h>

using namespace std;

string solve()
{
	int counter[30];
	for(int i=0; i<30; ++i)
		counter[i] = 0;
		
	char tab[2500];
	scanf("%s", tab);
	int len = strlen(tab);
	
	for(int i=0; i<len; ++i)
		counter[ tab[i]-'A']++;
	
	int digits[10];
	for(int i=0; i<10; ++i)
		digits[i] = 0;
	
	digits[2] = counter['W'-'A'];
	counter['T'-'A'] -= counter['W'-'A'];
	counter['O'-'A'] -= counter['W'-'A'];
	counter['W'-'A'] -= counter['W'-'A'];
	
	digits[0] = counter['Z'-'A'];
	counter['E'-'A'] -= counter['Z'-'A'];
	counter['R'-'A'] -= counter['Z'-'A'];
	counter['O'-'A'] -= counter['Z'-'A'];
	counter['Z'-'A'] -= counter['Z'-'A'];

	digits[6] = counter['X'-'A'];
	counter['S'-'A'] -= counter['X'-'A'];
	counter['I'-'A'] -= counter['X'-'A'];
	counter['X'-'A'] -= counter['X'-'A'];
	
	digits[8] = counter['G'-'A'];
	counter['E'-'A'] -= counter['G'-'A'];
	counter['I'-'A'] -= counter['G'-'A'];
	counter['H'-'A'] -= counter['G'-'A'];
	counter['T'-'A'] -= counter['G'-'A'];
	counter['G'-'A'] -= counter['G'-'A'];
	
	digits[7] = counter['S'-'A'];
	counter['E'-'A'] -= counter['S'-'A'];
	counter['V'-'A'] -= counter['S'-'A'];
	counter['E'-'A'] -= counter['S'-'A'];
	counter['N'-'A'] -= counter['S'-'A'];
	counter['S'-'A'] -= counter['S'-'A'];
	
	digits[5] = counter['V'-'A'];
	counter['F'-'A'] -= counter['V'-'A'];
	counter['I'-'A'] -= counter['V'-'A'];
	counter['E'-'A'] -= counter['V'-'A'];
	counter['V'-'A'] -= counter['V'-'A'];
	
	digits[4] = counter['F'-'A'];
	counter['O'-'A'] -= counter['F'-'A'];
	counter['U'-'A'] -= counter['F'-'A'];
	counter['R'-'A'] -= counter['F'-'A'];
	counter['F'-'A'] -= counter['F'-'A'];
	
	digits[1] = counter['O'-'A'];
	counter['N'-'A'] -= counter['O'-'A'];
	counter['E'-'A'] -= counter['O'-'A'];
	counter['O'-'A'] -= counter['O'-'A'];	
		
	digits[9] = counter['N'-'A']/2;
	counter['I'-'A'] -= counter['N'-'A']/2;
	counter['E'-'A'] -= counter['N'-'A']/2;
	counter['N'-'A'] -= counter['N'-'A'];
	
	digits[3] = counter['T'-'A'];
	
	
	string s;
	
	for(int i=0; i<10; ++i)
		for(int j=0; j<digits[i]; ++j)
			s = s+ (char)('0' + i);
			
	return s;
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int i=1; i<=tests; ++i)
	{
		string s = solve();
		printf("Case #%d: ", i);
		cout<<s<<"\n";
	}
	return 0;	
}
