#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		int d;
		cin >> d;
		vector<int> vals(d);
		for (int i=0;i<d;i++) {
			cin >> vals[i];
		}

		sort(vals.rbegin(), vals.rend());
		int best = -1;
		for (int h=1;h<=vals[0];h++) {
			int count = 0;
			for (int i=0;i<d;i++) {
				if (vals[i] > h)
					count += (vals[i] + h - 1) / h - 1;
			}

			int time = h + count;
			if (best == -1 || time < best)
				best = time;
		}

		cout << "Case #" << (q + 1) << ": " << best << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}