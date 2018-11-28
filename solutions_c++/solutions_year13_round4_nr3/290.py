#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <map>

using namespace std;

int ans[2010];
int n;
int a[2010];
int b[2010];
bool used[2010];
bool found;

bool check () {
	for (int i=n-1; i>=0; i--) {
		if (b[i]==1) {
			for (int j=i+1; j<n; j++) {
				if (ans[j] < ans[i])
					return false;
			}
		}
		else {
			bool valid = false;
			for (int j=i+1; j<n; j++) {
				if (ans[j] < ans[i] && b[j] >= b[i])
					return false;
				if (ans[j] < ans[i] && b[j] == b[i]-1)
					valid = true;
			}

			if (!valid)
				return false;
		}
	}
	return true;
}

void DFS (int step) {
	if (found)
		return;
	int count = 0;

	if (step==n && check()) {
		found = true;
		for (int i=0; i<step; i++)
			cout << " " << ans[i]+1;
		return;
	}
	else if (step==n)
		return;

	for (int i=0; i<n; i++) {
		if (!used[i])
			count++;
		if (used[i])
			continue;
		if (count >= b[step]) {
			bool valid = false;
			if (a[step]==1) {
				valid = true;
				for (int j=0; j<step; j++) {
					if (ans[j] < i) {
						valid = false;
						break;
					}
				}
			}
			else {
				for (int j=0; j<step; j++) {
					if (ans[j] < i && a[j] >= a[step]) {
						valid = false;
						break;
					}
					if (ans[j] < i && a[j] == a[step]-1) {
						valid = true;
					}
				}
			}
			if (valid) {
				used[i] = true;
				ans[step] = i;
				DFS (step+1);
				used[i] = false;
			}
		}
	}

}

void solve(int testcase) {
	cout << "Case #" << testcase << ":";
	cin >> n;
	for (int i=0; i<n; i++) {
		used[i] = false;
		cin >> a[i];
	}
	for (int i=0; i<n; i++) {
		cin >> b[i];
	}

	found = false;
	DFS (0);

	if (!found)
		cerr << " not found" << endl;

	cout << endl;
}

int main () {
	int testcases;

	cin >> testcases; 

	for (int testcase=1; testcase<=testcases; testcase++) {
		solve(testcase);
	}
	return 0;
}
