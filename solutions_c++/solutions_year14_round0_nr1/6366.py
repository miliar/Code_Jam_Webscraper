#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cout << "Case #" << tt << ": ";
		int k, x;
		set<int> cur;
		cin >> k;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				cin >> x;
				if (i + 1 == k) cur.insert(x);
			}
		cin >> k;
		set<int> cur2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				cin >> x;
				if (i + 1 == k && cur.count(x)) cur2.insert(x);
			}
		if (cur2.size() == 1) cout << *cur2.begin()	<< endl;
		if (cur2.size() > 1) cout << "Bad magician!\n";
		if (cur2.size() == 0) cout << "Volunteer cheated!\n";
	}
}