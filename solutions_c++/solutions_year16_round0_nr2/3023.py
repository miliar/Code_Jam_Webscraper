#include <bits/stdc++.h>
#ifdef DEBUG
#define D(x...) fprintf(stderr,x) 
#else
#define D(x...)
#endif
using namespace std;
int T; 
char S[200];
int main ()
{
	freopen("infile.txt", "r", stdin);
	freopen("outfile.txt", "w", stdout);
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		scanf(" %s ", S);
		int cnt=1;
		for(int s=1; s<strlen(S); s++)
		{
			if(S[s] != S[s-1])
			{
				cnt++;
			}
		}
		if(S[strlen(S)-1]=='+')
		{
			cnt--;
		}
		printf("Case #%d: %d\n",t, cnt);
		D("solved %d\n", t);
	}
}