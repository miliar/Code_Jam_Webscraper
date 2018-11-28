#include <cstdio>
#include <string>
using namespace std;
const int MAXN=1000;
char s[MAXN+7];
int main ()
{
	int t; scanf ("%d", &t);
	for (int i=1; i<=t; i++)
	{
		int n; scanf ("%d", &n);
		scanf ("%s", &s);
		int ans=0, sum=s[0]-'0';
		for (int j=1; j<=n; j++)
		{
			if (sum < j)
			{
				ans += (j-sum);
				sum = j;
			}
			sum += s[j]-'0';
			
		}
		printf ("Case #%d: %d\n", i, ans);
	}
	return 0;
}
