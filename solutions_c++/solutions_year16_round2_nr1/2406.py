#include <bits/stdc++.h>
#ifdef DEBUG
#define D(x...) fprintf(stderr,x) 
#else
#define D(x...)
#endif
using namespace std;
int T, N;
int freq[10][30];
string nums[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int order[10]={0, 2, 6, 7, 4, 5, 8, 3, 1, 9};
char lets[10]={'Z', 'W', 'X', 'S', 'U', 'V', 'G', 'R', 'O', 'I'};
int main()
{
	freopen("infile.txt", "r", stdin);
	freopen("outfile.txt", "w", stdout);
	scanf("%d", &T);
	for(int i=0; i<10; i++)
	{
		for(auto c: nums[i])
		{
			freq[i][c-'A']++;
		}
	}
	for(int t=1; t<=T; t++)
	{
		int inpf[30];
		for(int i=0; i<26; i++)
		{
			inpf[i]=0;
		}
		char inp[4000];
		scanf(" %s ", inp);
		for(int i=0; i<strlen(inp); i++)
		{
			inpf[inp[i]-'A']++;
		}
		int F[10];
		for(int i=0; i<10; i++)
		{
			F[i]=0;
		} 
		for(int i=0; i<10; i++)
		{
			int x = order[i];
			char c = lets[i];
			F[x]= inpf[c-'A'];
			for(int a=0; a<26; a++)
			{
				inpf[a]-= freq[x][a]*F[x];
			}
		}
		printf("Case #%d: ", t);
		for(int i=0; i<10; i++)
		{
			for(int f=0; f<F[i]; f++)
			{
				printf("%d", i);
			}
		}
		printf("\n");
	}
}