#include <assert.h>
#include <cstring>
#include <iostream>
#include <fstream>
#include <climits>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

std::vector<int> v;

int main() {
	int cases;
	cin >> cases;
	for (int t = 1; t <= cases; t++)
	{
		int n, x;
		cin >> n >> x;
		v.clear();
		for (int i = 0; i < n; i ++)
		{
			int a;
			cin >> a;
			v.push_back(a);
		}
		sort(v.begin(), v.end());
		int l = 0, r = v.size()-1;
		int sum = 0;

		//for (int i = 0; i < n; i ++) cout << v[i] << " ";
		//cout << endl;
		while (l < r)
		{
			if (v[l] + v[r] <= x)
			{
				l ++;
				r --;
				sum++;
			}
			else 
			{
				r--;
				sum++;
			}
		}
		if ( l == r) sum++;
		printf("Case #%d: %d\n", t, sum);
	}
	return 0;
}