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
		int n,x;
		cin >> n >> x;
		vector<int> vals(n);
		for (int i=0;i<n;i++) {
			cin >> vals[i];
		}

		sort(vals.rbegin(), vals.rend());
		vector<bool> used(n, false);
		int res = 0;
		for (int i=0;i<n;i++) {
			if (used[i])
				continue;
			int first = vals[i];
			used[i] = true;
			int second = -1;
			for (int j=i+1;j<n;j++) {
				if (used[j])
					continue;
				if (first + vals[j] <= x) {
					second = j;
					used[second]=true;
					break;
				}
			}
			res++;
		}

		cout << "Case #" << (q + 1) << ": " << res << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}