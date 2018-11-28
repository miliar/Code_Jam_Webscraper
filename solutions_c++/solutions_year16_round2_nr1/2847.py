#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cstring>

int count[27];
int res[10];

const char *nums[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
const int order[10] = { 0, 4, 3, 2, 1, 6, 8, 7, 5, 9 };

int requis[10][27];

void backtrack(int rest)
{
	if(rest==0)
		return; //fini
	
	for(int i = 0; i < 10; i++)
	{
		int quel = order[i];
		
		bool ok = true;
		
		for(int j = 0; j < 26; j++)
			if(count[j] < requis[quel][j])
				ok = false;
		
		if(ok==false)
			continue;
		
		for(int j = 0; j < 26; j++)
		{
			count[j] -= requis[quel][j];
			rest -= requis[quel][j];
		}
		
		res[quel]++;
		backtrack(rest);
		break;
	}
}

int main()
{
	for(int i = 0; i < 10; i++)
	{
		int p = strlen(nums[i]);
		
		for(int j = 0; j < p; j++)
			requis[i][nums[i][j]-'A']++;
	}

	int T;
	scanf("%d", &T);
	
	for(int t = 1; t <= T; t++)
	{
		char str[2016];
		scanf("%s", str);
		
		int S = strlen(str);
		
		for(int i = 0; i < S; i++)
			count[str[i]-'A']++;
		
		backtrack(S);
		
		printf("Case #%d: ", t);
		for(int i = 0; i < 10; i++)
			for(int j = 0; j < res[i]; j++)
				putchar((char)(i+'0'));
		putchar('\n');
		
		for(int i = 'A'; i <= 'Z'; i++)
			count[i-'A']=0;
		for(int i = 0; i < 10; i++)
			res[i]=0;
	}
	
	return 0;
}
