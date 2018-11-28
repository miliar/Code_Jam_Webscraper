#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
using namespace std;
int main()
{
	int t = 0, T;
	scanf("%d", &T);
	while(t++ < T)
	{
		int a, b, k;
		scanf("%d%d%d", &a, &b, &k);
		int br = 0;
		for(int i = 0; i < a; i++)
			for(int j = 0; j < b; j++)
				if((i & j) < k) br++;
		printf("Case #%d: %d\n", t, br);
	}
	return 0;
}
