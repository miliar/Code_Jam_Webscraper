#include <iostream>
#include <algorithm>
#include <set>
#include <functional>
using namespace std;

#define MAX 1000

int main()
{
	int n;
	long long x;
	long long a = 0;
	int b;
	int count = 1;
	set<int> diff;
	pair<set<int>::iterator, bool> check;
	freopen("A-large.in", "rt", stdin);
	freopen("Output", "wt", stdout);
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%I64d", &x);
		if(x == 0)
		{
			printf("Case #%d: INSOMNIA\n", i+1);
		}
		else
		{
			while(diff.size() != 10)
			{
				a = count * x;
				while(a != 0)
				{
					b = a % 10;
					a = a / 10;
					diff.insert(b);				
				}
				if(diff.size() != 10)
				{
					count++;
				}
				else
				{
					printf("Case #%d: %d\n", i+1, count*x);
					break;
				}
			}
			diff.clear();
			x = 0;
			a = 0;
			count = 1;
		}

	}
	return 0;
}