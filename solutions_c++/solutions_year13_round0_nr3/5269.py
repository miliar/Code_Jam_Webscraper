#include <stdio.h>
#include <algorithm>
#include <string>
using namespace std;

bool ispalindrome(int n)
{
	char str[100];
	sprintf(str, "%d", n);
	string str2 = str;
	reverse(str2.begin(), str2.end());
	return str2 == str;
}

bool P[1005];
bool P2[1005];
int sum[1005];

int main()
{
	freopen("C:\\temp\\c.in","r",stdin);
	freopen("C:\\temp\\c.out","w",stdout);
	for(int i = 1; i <= 1000; i++) P[i] = ispalindrome(i);
	for(int i = 1; i * i <= 1000; i++)
	{
		if (P[i] && P[i*i]) P2[i*i] = true;
	}
	int T;
	scanf("%d",&T);
	for (int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ", TT);
		int ans = 0, a, b;
		for (scanf("%d%d",&a,&b); a <= b; a++)
		{
			if (P2[a]) ans++;
		}
		printf("%d\n", ans);
	}
	return 0;
}