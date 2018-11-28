#include <iostream>
#include <set>
#include <limits.h>
using namespace std;

#define FOR(i, s, n) for(unsigned long long i = (s); i < (n); i++)
#define pl(x) cout << x << endl

void main()
{
	int T;
	cin >> T;
	FOR(cases, 1, T + 1)
	{
		set<int> nums;
		unsigned long long N, ans, tmp;
		bool end = false;
		cin >> N;

		if (N == 0)
		{
			printf("Case #%d: INSOMNIA\n", cases);
			continue;
		}			

		unsigned long long max = ULLONG_MAX / N;
		FOR(i, 1, max)
		{
			if (end)
				break;

			ans = N * i;
			tmp = ans;
			while (tmp != 0)
			{
				nums.insert(tmp % 10);
				if (nums.size() == 10)
				{
					end = true;
					break;
				}
				tmp /= 10;
			}
		}		
		if (end)
			cout << "Case #" << cases << ": " << ans << endl;		
		else
			cout << "Case #" << cases << ": INSOMNIA" << endl;			
	}
}