#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <set>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		int n;
		cin >> n;
		vector<double> a(n),b(n);
		for (int i=0;i<n;i++) {
			cin >> a[i];
		}
		for (int i=0;i<n;i++) {
			cin >> b[i];
		}

		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		int war_count = 0;
		vector<bool> bused(n, false);
		for (int i=0;i<n;i++) {
			int use = -1;
			for (int j=0;j<n;j++) {
				if (bused[j]) continue;
				if (use == -1) use = j;
				if (b[j] > a[i]) {
					use = j;
					war_count++;
					break;
				}
			}
			bused[use] = true;
		}

		int dec = 0;
		for (int i=0;i<n;i++) {
			if (b[0] > a[0]) {
				a.erase(a.begin());
				b.erase(b.begin() + b.size() - 1);
			}
			else {
				dec++;
				a.erase(a.begin());
				b.erase(b.begin());
			}
		}

		cout << "Case #" << (q+1) << ": " << dec << " " << (n - war_count) << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}