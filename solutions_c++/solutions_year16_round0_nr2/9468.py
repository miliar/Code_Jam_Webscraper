#include <iostream>
#include <string>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);

	int T,ans;
	char curr;
	string str;
	scanf("%d",&T);
	for(int tt = 1; tt <= T; tt++)
	{
		ans = 0;
		cin >> str;
		curr = str[0];
		for(int i = 0; i < str.size(); i++)
		{	
			if(str[i] != curr)
			{
				ans++;
				curr = str[i];
			}
		}
		if(curr == '-')
			ans++;

		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}