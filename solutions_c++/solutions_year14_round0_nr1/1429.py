#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

int a[16];
set<int> sel;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 0; t < T; ++t)
	{
		int ans;
		cin >> ans;
		--ans;
		for(int i = 0; i < 16; ++i)
		{
			cin >> a[i];
		}
		sel.clear();
		for(int i = 0; i < 4; ++i)
		{
			sel.insert(a[i + ans*4]);
		}
		
		cin >> ans;
		--ans;
		for(int i = 0; i < 16; ++i)
		{
			cin >> a[i];
		}
		int result = -2;
		for(int i = 0; i < 4; ++i)
		{
			if(sel.find(a[i + ans*4]) != sel.end())
			{
				if(result == -2)
				{
					result = a[i + ans*4];
				}
				else
				{
					result = -1;
				}
			}
		}
		if(result == -1)
		{
			cout << "Case #" << t + 1 << ": Bad magician!\n";
		}
		else if (result == -2)
		{
			cout << "Case #" << t + 1 << ": Volunteer cheated!\n";
		}
		else
		{
			cout << "Case #" << t + 1 << ": " << result << endl;
		}
	}
	return 0;
}
