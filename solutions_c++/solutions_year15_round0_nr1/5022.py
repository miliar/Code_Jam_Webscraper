#include<bits/stdc++.h>
using namespace std;
char A[1005];
int S[1005];
int main()
{
int t; scanf("%d", &t);
for(int k = 1; k <= t; k++)
{
		int n; scanf("%d", &n);
		scanf("%s", A);
	
	for(int i = 0; i <= n; i++)
		S[i] = A[i] - '0';
	
	int razem = S[0];
	int ans = 0;
	for(int i = 1; i <= n; i++)
	{
		if(razem >= i)
			razem += S[i];
		else
		{
			ans += (i - razem);
			razem += (i - razem);
			razem += S[i];
		}
	}
	printf("Case #%d: %d\n",k, ans);
}
return 0;
}