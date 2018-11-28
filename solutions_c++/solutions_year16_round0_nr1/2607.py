#include <stdio.h>
#include <set>
#define ll long long
using namespace std;

int main()
{
	int T, N, digit, nt = 0;
	ll int number, orig_number;
	scanf("%d", &T);
	while(nt < T)
	{
		scanf("%d", &N);
		int res = -1;
		if (N > 0)
		{
			set<int> digits;
			int i =1;
			while(res < 0)
			{
				number = i*N;
				orig_number = number;
				while(number>0)
				{
					digit = number % 10;
					number = number / 10; 
					digits.insert(digit);
					if (digits.size() == 10)
					{
						res = orig_number;
						break;
					}
				}
				i++;
			}
		}
		nt++;
		if (res >= 0)
		{
			printf("Case #%d: %d\n", nt ,res);
		} else {
			printf("Case #%d: INSOMNIA\n", nt);
		}

	}
}