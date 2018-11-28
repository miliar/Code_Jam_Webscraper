#include <stdio.h>
#include <set>
#include <vector>
using namespace std;

int main()
{
	set<int> result;
	long long k;
	vector<long long> tmp;
	int t, n, countCase = 1;
	freopen("INPUT.INP", "rt", stdin);
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d", &n);
		if (n == 0){
			tmp.push_back(-1);
		}
		else
		{
			for (int i = 1; true; i++)
			{
				k = i * n;
				while (k > 0)
				{
					result.insert(k % 10);
					k /= 10;
				}
				if (result.size() >= 10)
				{
					tmp.push_back(i * n);
					break;
				}
			}
		}
		result.clear();
	}

	t = tmp.size();
	freopen("Output.out", "wt", stdout);
	for (int i = 0; i < t; i++)
		if (tmp[i] == -1)
			printf("Case #%d: INSOMNIA\n", i + 1);
		else
			printf("Case #%d: %I64d\n", i + 1, tmp[i]);

	return 0;
}