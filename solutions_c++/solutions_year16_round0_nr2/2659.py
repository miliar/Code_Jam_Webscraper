#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

void flip(vector<int>& pancakes, int k)
{
	int n = pancakes.size();
	vector<int> list(n-k);
	for (int i = 0; i < n-k; ++i)
	{
		list[i] = pancakes[n-i-1];
	}
	for (int i = k; i < n; ++i)
	{
		if (list[i-k]==1)
			pancakes[i] = 0;
		else
			pancakes[i] = 1;
	}
}

int solve(vector<int>& pancakes)
{
	int nextbase, base;
	base = 0;
	int top = pancakes.size()-1;
	int nops = 0;
	nextbase = -1;
	while(pancakes[base]==1)
	{
		base++;
	}
	while (base < top || (base == top && pancakes[top]==0))
	{
		if (pancakes[top] == 0) // flip to set base +
		{
			flip(pancakes, base);
			nops++;
		} else {  // pancakes[top] == 1
			nextbase = base + 1;
			while (pancakes[nextbase]==0) // flip starting from +
			{
				nextbase++;
			}
			flip(pancakes, nextbase);
			nops++;
		}
		while(pancakes[base]==1)
		{
			base++;
		}
	}
	return nops;
}

int main()
{
	int T, n, nt;
	nt = 0;
	cin >> T;
	while(nt < T)
	{
		// read input string
		string str;
		cin >> str;
		n = str.size();
		vector<int> pancakes(n);
		reverse(str.begin(),str.end());
		
		for (int i = 0; i < n; ++i)
		{
			if (str[i] == '+')
			{
				pancakes[i] = 1;
			}
		}
		int nops = solve(pancakes);

		nt++;
		cout << "Case #" << nt << ": " << nops << endl;
	}
}