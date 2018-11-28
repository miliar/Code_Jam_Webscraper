#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int T,S;

int main()
{
	scanf("%d",&T);
	for(int z=0; z < T; z++)
	{
		scanf("%d",&S);
		string s;
		cin>>s;

		int sum = 0;
		int res = 0;
		for(int i = 0; i <= S; i++)
		{
			res += max(0,i-sum);
			sum = max(sum,i);
			sum += (int)(s[i]-'0');
		}

		printf("Case #%d: %d\n",z+1,res);
	}

	return 0;
}