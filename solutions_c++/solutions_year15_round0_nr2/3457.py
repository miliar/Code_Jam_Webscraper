#include <bits/stdc++.h>
using namespace std;

constexpr size_t special_minutes(size_t to_distribute, size_t maximum)
{
	return (to_distribute-1)/maximum;
}

void test()
{
	size_t N;
	cin >> N;
	vector<size_t> data(1001);
	
	for (size_t i=1; i<=N; ++i)
	{
		size_t tmp;
		cin >> tmp;
		++data[tmp];
	}
		
	size_t best_cost = 1000;
	for (size_t m=1000; m>=1; --m)//maximum pancakes on plates after moving all
	{
		size_t cost = m;
		for (size_t i=m+1; i<=1000; ++i)//will move away some pancakes from these people
		{
			if (data[i]==0) continue;//optimization
			
			cost += data[i]*special_minutes(i, m);
		}
		best_cost = min(cost, best_cost);
	}
	
	cout << best_cost;
}

int main()
{
	size_t c;
	cin >> c;
	for (size_t i = 1; i<=c; ++i)
	{
		cout << "Case #" << i << ": ";
		test();
		cout << endl;
	}
}
