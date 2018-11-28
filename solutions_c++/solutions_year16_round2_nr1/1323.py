// GETTING the digits


#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define M 26
#define N 10

int cnt[M];
int ans[N];

void init()
{
	for(int i = 0; i < M; ++i)
	{
		cnt[i] = 0;
	}
	for(int i = 0; i < N; ++i)
	{
		ans[i] = 0;
	}
	return;
}

int main()
{
	int tc, cs = 1;
	cin >> tc;
	
	while(tc--)
	{
		string str;
		cin >> str;
		init();
		int sz = (int)str.size();
		
		for(int i = 0; i < sz; ++i)
		{
			cnt[str[i] - 'A']++;
		}
		int p;
		if(p = cnt['Z' - 'A']) // 0
		{
			cnt['Z' - 'A'] -= p;
			cnt['E' - 'A'] -= p;
			cnt['R' - 'A'] -= p;
			cnt['O' - 'A'] -= p;
			ans[0] += p;
		}
		if(p = cnt['W' - 'A']) // 2
		{
			cnt['T' - 'A'] -= p;
			cnt['W' - 'A'] -= p;
			cnt['O' - 'A'] -= p;
			ans[2] += p;
		}
		if(p = cnt['U' - 'A']) // 4
		{
			cnt['F' - 'A'] -= p;
			cnt['O' - 'A'] -= p;
			cnt['U' - 'A'] -= p;
			cnt['R' - 'A'] -= p;
			ans[4] += p;
		}
		if(p = cnt['X' - 'A']) // 6
		{
			cnt['S' - 'A'] -= p;
			cnt['I' - 'A'] -= p;
			cnt['X' - 'A'] -= p;
			ans[6] += p;
		}
		if(p = cnt['G' - 'A']) // 8
		{
			cnt['E' - 'A'] -= p;
			cnt['I' - 'A'] -= p;
			cnt['G' - 'A'] -= p;
			cnt['H' - 'A'] -= p;
			cnt['T' - 'A'] -= p;
			ans[8] += p;
		}
		if(p = cnt['H' - 'A']) // 3
		{
			cnt['T' - 'A'] -= p;
			cnt['H' - 'A'] -= p;
			cnt['R' - 'A'] -= p;
			cnt['E' - 'A'] -= p;
			cnt['E' - 'A'] -= p;
			ans[3] += p;
		}
		if(p = cnt['O' - 'A']) // 1
		{
			cnt['O' - 'A'] -= p;
			cnt['N' - 'A'] -= p;
			cnt['E' - 'A'] -= p;
			ans[1] += p;
		}
		if(p = cnt['F' - 'A']) // 5
		{
			cnt['F' - 'A'] -= p;
			cnt['I' - 'A'] -= p;
			cnt['V' - 'A'] -= p;
			cnt['E' - 'A'] -= p;
			ans[5] += p;
		}
		if(p = cnt['V' - 'A']) // 7
		{
			cnt['S' - 'A'] -= p;
			cnt['E' - 'A'] -= p;
			cnt['V' - 'A'] -= p;
			cnt['E' - 'A'] -= p;
			cnt['N' - 'A'] -= p;
			ans[7] += p;
		}
		if(p = cnt['I' - 'A']) // 9
		{
			cnt['N' - 'A'] -= p;
			cnt['I' - 'A'] -= p;
			cnt['N' - 'A'] -= p;
			cnt['E' - 'A'] -= p;
			ans[9] += p;
		}
		printf("Case #%d: ", cs++);
		for(int i = 0; i < N; ++i)
		{
			for(int j = 0; j < ans[i]; ++j)
			{
				printf("%d", i);
			}
		}
		printf("\n");
	}
	return 0;
}









