#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

int minTime(int step, priority_queue<int> pies)
{
	if (step > 9) return 10000000;
	int mx = pies.top();
	if(mx < 4) return step + mx;
	pies.pop();
	int ans = step + mx;
	for(int i = 1; i <= mx / 2; ++i)
	{
		priority_queue<int> pies1 = pies;
		pies1.push(i);
		pies1.push(mx - i);
		ans = min(ans, minTime(step + 1, pies1));
	}
	return ans;
}	

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		priority_queue<int> pies;
		int d, tmp;
		cin >> d;
		for(int j = 0; j < d; ++j)
		{
			cin >> tmp;
			pies.push(tmp);
			//cout << tmp << " ";
		}
		//cout << endl;
		printf("Case #%d: %d\n", i, minTime(0, pies));
	}
	return 0;
}
