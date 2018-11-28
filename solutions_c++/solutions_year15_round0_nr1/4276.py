#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <memory>

using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	
	
	int T;
	char str[1005];
	scanf("%d",&T);
	for(int t = 1; t<=T; t++)
	{
		int smax;
		scanf("%d",&smax);
		scanf("%s",&str);

		int aud = 0;
		int res = 0;
		for(int i = 0; i<=smax; i++)
		{
			int val = str[i] - '0';
			if(val>0) 
			{
				if(aud < i) 
				{
					res += i-aud;
					aud = i+val;
				}
				else 
				{
					aud += val;
				}
			}
		}
		printf("Case #%d: %d\n",t,res);
	}
}
