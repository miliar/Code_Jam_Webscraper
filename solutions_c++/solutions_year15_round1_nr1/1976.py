#include <vector>
#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	freopen("/mnt/S/Code/in.txt", "rt", stdin);
	freopen("/mnt/S/Code/out.txt", "wt", stdout);

	int cases; cin >> cases;
	int n, x;
	vector<int> v;
	int cnt = 0;
	for (int i = 0; i < cases; ++i)
	{
		cnt++;
		v.clear();
		cin >> n;
		for (int j = 0; j < n; ++j)
		{
			cin >> x;
			v.push_back(x);
		}
		//the second method
		//get minimum
		int max = 0;
		int diff;
		int sum2 = 0;
		for (int j = 0; j < n - 1 ; ++j)
		{
			diff = v[j] - v[j + 1];
			if (diff > 0)sum2 += diff;
			if (diff > max)max = diff;
		}
		int sum = 0;
		for (int j = 0; j < n - 1; ++j)
		{
			if (v[j] > max) {
				sum += max;
			} else {
				sum += v[j];
			}
		}
		cout << "Case #" << cnt << ": " << sum2 << " " << sum << endl;



	}
	return 0;
}
