#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

int calc_friends(const int num, const char *audi)
{
	int stands = audi[0] - '0';

	int lacks = 0;
	for(int lv = 1; lv <= num; ++lv)
	{
		int n_audi = audi[lv] - '0';
				
		if(n_audi > 0)
		{
			int need = 0;
			if(lv > stands)
				need += lv - stands;

			lacks += need;
			stands += n_audi + need;
		}
	}

	return lacks;
}

int main()
{
	int T = 0;
	scanf("%d", &T);


	int num_case = 1;
	while(T-->0)
	{
		int num = 0;
		char buf_audi[2000];
		scanf("%d %s", &num, buf_audi);
		
		int num_invite = calc_friends(num, buf_audi);
		printf("Case #%d: %d\n", num_case, num_invite);

		++num_case;
	}
	return 0;
}