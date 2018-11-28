#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	int t,j;
	char str[105];
	scanf("%d",&t);
	j = t;
	while(t--)
	{
		scanf("%s",str);
		int i, len = 0, cnt = 0;
		for( i = 0 ; str[i] != '\0' ; i++ )
		{
			len++;
		}
		for( i = 0 ; i < len - 1 ; i++ )
		{
			if(str[i] != str[i + 1])
			{
				cnt++;
			}
		}
		if(str[len - 1] == '-' )
		{
			cnt++;
		}
		printf("Case #%d: %d\n",j - t, cnt);
	}
	return 0;
}
