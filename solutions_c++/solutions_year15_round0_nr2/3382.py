#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#define pb push_back
#define NMAX 1005
#define INF 0x3f3f3f3f
using namespace std;
int tests, n, A[NMAX];
vector <int> curr;

bool comp(int x, int y)
{
	return x > y;
}

int main()
{
	freopen("pancaces.in", "r", stdin);
	freopen("pancaces.out", "w", stdout);
	
	cin >> tests;
	for (int test_no = 1; test_no <= tests; test_no++)
	{
		cout << "Case #" << test_no << ": ";
		
		cin >> n;
		int best = 0;
		for (int i = 1; i <= n; i++)
		{
			cin >> A[i];
			best = max(best, A[i]);
		}
		
		for (int steps = 0; steps <= 1000; steps++)
		{
			for (int t = steps + 1; t <= 1000; t++)
			{
				int currSteps = 0;
				for (int i = 1; i <= n; i++)
				{
					int val = A[i] / (t - steps);
					if (A[i] % (t - steps))
						val++;
						
					currSteps += val - 1;
				}
				if (currSteps <= steps)
					best = min(best, t);
			}
		}
		
		cout << best << "\n";
	}
	return 0;
}
