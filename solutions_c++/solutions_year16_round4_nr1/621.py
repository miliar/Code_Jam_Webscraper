#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>


std::vector<int> build(int level, int top)
{
	if(level == 0)
		return std::vector<int>(1, top);

	std::vector<int> a = build(level - 1, top);
	std::vector<int> b = build(level - 1, (top + 2) % 3);
	if(a > b)
		std::swap(a, b);

	for(size_t i = 0; i < b.size(); i++)
		a.push_back(b[i]);

	return a;
}


std::vector<int> data;

bool solve(int level, int p, int r, int s)
{
	for(int top = 0; top < 3; top++)
	{
		std::vector<int> seq = build(level, top);
		int cnt[3] = {0, 0, 0};
		for(size_t i = 0; i < seq.size(); i++)
			cnt[ seq[i] ]++;

		if(cnt[0] == p && cnt[1] == r && cnt[2] == s)
		{
			data = seq;
			return true;
		}
	}

	return false;
}


const char subst[3] = {'P', 'R', 'S'};

int main()
{
	int tests;
	scanf("%i\n", &tests);

	for(int test = 1; test <= tests; test++)
	{
		int n, r, p, s;
		scanf("%i %i %i %i\n", &n, &r, &p, &s);

		printf("Case #%i: ", test);

		if(solve(n, p, r, s))
		{
			for(int i = 0; i < (int)data.size(); i++)
				printf("%c", subst[ data[i] ]);
			printf("\n");
		}
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}

