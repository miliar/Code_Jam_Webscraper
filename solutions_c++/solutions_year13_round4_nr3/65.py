#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

void solve()
{
	int n;
	cin >> n;

	vector < int > a(n), b(n);

	for(int i = 0; i < n; i++) {
		cin >> a[i];
	}

	for(int i = 0; i < n; i++) {
		cin >> b[i];
	}

	const int inf = n + 1;

	vector < int > res(n, inf), aTemp(n), bTemp(n);
	vector < bool > bad(n);

	for(int num = 1; num <= n; num++) {
		fill(bad.begin(), bad.end(), false);

		for(int pos = 0; pos < n; pos++) {
			aTemp[pos] = 1;

			for(int other = 0; other < pos; other++) {
				if(res[other] < res[pos])
					aTemp[pos] = max(aTemp[pos], aTemp[other] + 1);
				if(res[pos] == inf && res[other] == inf && aTemp[other] >= a[pos])
					bad[other] = true;
			}		
		}

		for(int pos = n - 1; pos >= 0; pos--) {
			bTemp[pos] = 1;

			for(int other = pos + 1; other < n; other++) {
				if(res[other] < res[pos])
					bTemp[pos] = max(bTemp[pos], bTemp[other] + 1);
				if(res[pos] == inf && res[other] == inf && bTemp[other] >= b[pos])
					bad[other] = true;
			}
		}

		int resPos = -1;

		for(int pos = 0; pos < n && resPos == -1; pos++) {
			if(!bad[pos] && aTemp[pos] == a[pos] && bTemp[pos] == b[pos] && res[pos] == inf)
				resPos = pos;
		}

		assert(resPos != -1);

		res[resPos] = num;
	}

	for(int i = 0; i < n; i++)
		cout << res[i] << " \n"[i + 1 == n];
}

int main()
{
	int n;
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}

	return 0;
}