#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int fair (vector<double> &a, vector<double> &b)
{
	int used[1001] = {0};
	int naomi = 0;
	int n = a.size(); 

	for (int i = n-1; i >= 0; --i)
	{
		int best = -1;
		for (int j = 0; j < n; ++j)
		{
			if (b[j] > a[i] and  not used[j])
			{
				if (best == -1) best = j;
				else if (b[j] < b[best]) best = j;
			} 
		}			
		if (best == -1) {
			for (int i = 0; i < n; ++i) 
			{
				if (!used[i]) 
				{ 
					used[i] = 1;
					break;
				}
			}
			naomi++;
		} else 
		{
			used[best] = 1;
		}
	}
	return naomi;
}

int main (void)
{
	
	int t, caso = 1;
	cin >> t;

	while (t--)
	{
		int n;
		cin >> n;
		vector <double> a(n), b(n);
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		for (int i = 0; i < n; ++i)
			cin >> b[i];
		
		sort (a.begin(), a.end());
		sort (b.begin(), b.end()); 

		// for (int i = 0; i < a.size(); ++i)
			// cout << a[i] << " " << b[i] << endl;

		int naomi = fair(a, b);

		int deceit = 0;

		while (a.size())
		{
			if (a.front() > b.front()) 
			{
				a.erase(a.begin());
				b.erase(b.begin());
				deceit++;
			}
			else
			{
				a.erase(a.begin());
				b.pop_back();
			}
		}

		printf("Case #%d: %d %d\n", caso++, deceit, naomi);
	}

	return 0;
}
