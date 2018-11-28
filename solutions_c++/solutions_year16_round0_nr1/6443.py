#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t, n;
	long long b, a, k;
	scanf("%i", &t);
	for(int i=1;i<=t;i++)
	{
		k=1;
		set<int> S;
		int V[11]={0};
		scanf("%i", &n);
		if(n==0)
		{
			printf("CASE #%i: INSOMNIA\n", i);
			continue;
		}
		while(S.size()<=10)
		{
			if(S.size()==10)
				break;
			a=n*k;
			k++;
			b=a;
			while(a>0)
			{
				if(V[a%10]==0)
					V[a%10]++, S.insert(a%10);
				a/=10;
			}
		}
		printf("Case #%i: %ld\n", i, b);
	}
	return 0;
}