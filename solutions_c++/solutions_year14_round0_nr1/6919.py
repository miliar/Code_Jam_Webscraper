#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main()
{
	freopen("A-small-attempt1.in", "rt", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	for (int i = 0; i < T;i++)
	{
		int ans1, ans2;
		vector<vector<int> > a1(4, vector<int>(4, 0)), a2(4, vector<int>(4, 0));
		cin >> ans1;
		ans1--;
		for (int j = 0; j < 4;j++)
		    for (int k = 0; k < 4;k++)
		    {
				cin >> a1[j][k];
		    }
			cin >> ans2;
			ans2--;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{
				cin >> a2[j][k];
			}
			std::vector<int> v;

			sort(a1[ans1].begin(), a1[ans1].end());
			sort(a2[ans2].begin(), a2[ans2].end());

			std::set_intersection(a1[ans1].begin(), a1[ans1].end(), a2[ans2].begin(), a2[ans2].end(), back_inserter(v));

			size_t sz = v.size();

			cout << "Case #" << i + 1 << ": ";
			if (sz == 1)
			{
				cout << v[0];
			}
			else if (sz == 0)
			{
				cout << "Volunteer cheated!";
			}
			else if (sz > 1)
			{
				cout << "Bad magician!";
			}

			cout << endl;

	}
	return 0;
}

