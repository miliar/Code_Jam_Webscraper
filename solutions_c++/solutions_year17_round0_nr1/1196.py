#include <iostream>
#include <cstdio>
#include <cstring> 
using namespace std;

const int LMAX = 1023;

bool pcStat[LMAX];
int len;

void prtStat()
{
	for (int i = 0; i <= len; i++)
		printf("%d", pcStat[i]);
	printf("\n");
}

int main()
{
	/*freopen("qr17aL.in", "r", stdin);
	freopen("qr17aL.out", "w", stdout);*/
	int T, K, cnt, i;
	char S[LMAX];
	
	cin >> T;
	
	for (int cs = 1; cs <= T; cs++)
	{
		scanf("%s", S + 1);
		S[0] = '+';
		len = strlen(S);
		S[len] = '+';
		for (i = 1; i <= len; i++)
			pcStat[i] = S[i - 1] != S[i];
		
		cin >> K;
		
		cnt = 0;
		
		//prtStat();
		
		for (i = 1; i <= len - K; i++)
		{
			if (pcStat[i])
			{
				pcStat[i] ^= 1;
				pcStat[i + K] ^= 1;
				cnt++;
			}
			//prtStat();
		}
		
		for (i = len - K + 1; i <= len; i++)
			if (pcStat[i])
				break;
		if (i > len)
			printf("Case #%d: %d\n", cs, cnt);
		else
			printf("Case #%d: IMPOSSIBLE\n", cs);
		
	}
	return 0;
}


