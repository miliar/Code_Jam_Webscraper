#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
using namespace std;

typedef long long int lli;

int main(void)
{
	int t;
	scanf("%d", &t);

	for(int tt = 1;tt <= t;tt++)
	{
		lli n;
		scanf("%lld", &n);
		set<int> A;
		for(lli i = 0;i < 10;i++) A.insert(i);
		string tmp;
		bool done = false;
		for(lli i = 1;i <= 10000000;i++)
		{
			tmp = to_string(i*n);
			for(auto it: tmp) A.erase(int(it-'0'));
			if(A.empty())
			{
				printf("Case #%d: %lld\n", tt, i*n);
				done = true;
				break;
			}
		}
		if(!done) printf("Case #%d: INSOMNIA\n", tt);
	}
}