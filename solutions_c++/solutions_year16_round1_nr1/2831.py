#include <bits/stdc++.h>

using namespace std;

char s[1010];
string ans;
int main()
{
	int t, ind=0, n;
	scanf("%d",&t);
	while(t--)
	{
		ind++;
		scanf("%s",&s);
		printf("Case #%d: ", ind);
		n = strlen(s);
		ans = s[0];
		for(int i=1;i<n;i++)
		{
			if(ans[0] <= s[i])
				ans = s[i] + ans;
			else
				ans = ans + s[i];
		}
		cout << ans << endl;
	}
	return 0;
}