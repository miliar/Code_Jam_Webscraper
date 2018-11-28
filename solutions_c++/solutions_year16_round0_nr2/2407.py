#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main(void)
{
	string S;
	int t;
	scanf("%d", &t);
	for(int tt = 1;tt <= t;tt++)
	{
		cin >> S;

		reverse(S.begin(), S.end());

		int res = 0;
		for(auto it: S)
		{
			if(res%2 && it == '+') res++;
			else if(!(res%2) && it == '-') res++;
		}
		printf("Case #%d: %d\n", tt, res);
	}
}