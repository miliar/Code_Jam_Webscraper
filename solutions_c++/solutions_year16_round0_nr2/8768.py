#include <stdio.h>
#include <vector>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <iostream>
#include <map>
#include <iostream>
#include <set>
#include <string>
#include <queue>
#define ll long long int
#define s(x) scanf("%d",&x)
#define p(x) printf("%d ",x)

using namespace std;
int main()
{

	int t, i, tt;
	s(t);
	char S[1000];
	for( tt = 1; tt <= t; tt++)
	{
		printf("Case #%d: ", tt);
		scanf("%s",S);

		int ans = 0;
		for( i = 0; S[i]!= '\0' ; i++ )
		{
			if(S[i] == '+')
			{
				break;
			}
		}
		if( i > 0 )
			ans += 1;
		int flag = 0;

		for(;S[i]!= '\0' ; i++ )
		{
			if(S[i] == '-')
			{
				flag = 1;
			}
			if( S[i] == '+' && flag == 1)
			{
				ans += 2;
				flag = 0;
			}
		}
		if( flag == 1)
			ans += 2;
		printf("%d\n",ans );
	}
	return 0;
}