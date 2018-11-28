#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for(int j=1;j<=t;j++)
	{
		int n;
		scanf("%d", &n);
		string t;
		cin >> t;
		int wynik=0;
		int ile=t[0]-'0';
		for(int i=1;i<=n;i++)
		{
			int pr=0;
			if(t[i]-'0'>0 && ile<i)
			{
				pr=i-ile;
				wynik+=pr;
			}
			ile+=(t[i]-'0')+pr;
		}
		printf("Case #%d: %d\n", j, wynik);
	}
	return 0;
}