#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <queue>
using namespace std;
int T;
int lawn[101][101];
long long int N, M;
int Max = 0;
bool is_palindromes(long long int i)
{
	vector<int> all;
	while(i != 0) {
		all.push_back(i % 10L);
		i /= 10L;
	}
	for(int j = 0;j < all.size(); ++j) {
		if (all[j] != all[all.size() - j - 1])
			return false;
	}
	return true;
}
int main()
{
	freopen("..\\C-small-attempt0.in","r",stdin);
	freopen("..\\C-small-attempt0.out","w",stdout);
	scanf("%d",&T);

	for(int t = 1;t <= T;t++)
	{
		scanf("%lld", &N);
		scanf("%lld", &M);
		long long int left = sqrt((double)N);
		long long int right = sqrt((double)M);
		long long res = 0;
		for (long long int i = right; i >= left; --i) 
		{
			long long int sqr = i * i;
			if (sqr < N || sqr > M)
				continue;
			if (is_palindromes(i) && is_palindromes(sqr))
				res++;
		}
		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}