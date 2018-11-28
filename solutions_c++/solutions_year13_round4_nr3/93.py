#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <cassert>
using namespace std;
const int MAX_N = 2000 + 10;
int n, a[MAX_N], b[MAX_N];

/*
 * i<j
 */

vector<int> E[MAX_N]; //i>j
int ans[MAX_N];
int in[MAX_N];

bool used[MAX_N];

void work() {
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
	for (int i = 0; i < n; ++i) {
		cin >> b[i];
	}
	for (int i = 0; i < n; ++i) {
		E[i].clear();
	}
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			//i<j
			if (a[i] >= a[j]) {
				//Xj<Xi
				E[i].push_back(j);
			}
			if (b[j] >= b[i]) {
				//Xi<Xj
				E[j].push_back(i);
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		for (int j = i - 1; j >= 0; --j) {
			if (a[j] == a[i] - 1) {
				E[i].push_back(j);
				break;
			}
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			if (b[j] == b[i] - 1) {
				E[i].push_back(j);
				break;
			}
		}
	}

	memset(in, 0, sizeof in);
	for (int i = 0; i < n; ++i) {
		for (vector<int>::iterator e = E[i].begin(); e != E[i].end(); ++e) {
			in[*e]++;
		}
	}

	memset(used, 0, sizeof used);
	for (int i = n - 1; i >= 0; --i) {
		for (int j = n - 1; j >= 0; --j) {
			if (!used[j] && in[j] == 0) {
				ans[j] = i + 1;
				used[j] = true;

				for (vector<int>::iterator e = E[j].begin(); e != E[j].end();
						++e) {
					in[*e]--;
				}

				break;
			}
		}
	}

	cout << ans[0] << " ";
	for (int i = 1; i < n; ++i) {
		cout << ans[i] << " ";
	}
	cout << endl;
	int ca[MAX_N], cb[MAX_N];
	for (int i = 0; i < n; ++i) {
		ca[i] = 1;
		for (int j = 0; j < i; ++j)
			if (ans[j] < ans[i]) {
				ca[i] = max(ca[i], ca[j] + 1);
			}
	}
	for (int i = n - 1; i >= 0; --i) {
		cb[i] = 1;
		for (int j = i + 1; j < n; ++j) {
			if (ans[j] < ans[i]) {
				cb[i] = max(cb[i], cb[j] + 1);
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		assert(a[i] == ca[i]);
		assert(b[i] == cb[i]);
	}
}

void work2() {
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
	for (int i = 0; i < n; ++i) {
		cin >> b[i];
	}
	for (int i = 0; i < n; ++i) {
		E[i].clear();
	}
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			//i<j
			if (a[i] >= a[j]) {
				//Xj<Xi
				E[j].push_back(i);
			}
			if (b[j] >= b[i]) {
				//Xi<Xj
				E[i].push_back(j);
			}
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = i - 1; j >= 0; --j) {
			if (a[j] == a[i] - 1) {
				E[j].push_back(i);
				break;
			}
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			if (b[j] == b[i] - 1) {
				E[j].push_back(i);
				break;
			}
		}
	}

	memset(in, 0, sizeof in);
	for (int i = 0; i < n; ++i) {
		for (vector<int>::iterator e = E[i].begin(); e != E[i].end(); ++e) {
			in[*e]++;
		}
	}
	memset(used, 0, sizeof used);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (!used[j] && in[j] == 0) {
				ans[j] = i + 1;
				used[j] = true;

				for (vector<int>::iterator e = E[j].begin(); e != E[j].end();
						++e) {
					in[*e]--;
				}

				break;
			}
		}
	}

	cout << ans[0] << " ";
	for (int i = 1; i < n; ++i) {
		cout << ans[i] << " ";
	}
	cout << endl;
	int ca[MAX_N], cb[MAX_N];
	for (int i = 0; i < n; ++i) {
		ca[i] = 1;
		for (int j = 0; j < i; ++j)
			if (ans[j] < ans[i]) {
				ca[i] = max(ca[i], ca[j] + 1);
			}
	}
	for (int i = n - 1; i >= 0; --i) {
		cb[i] = 1;
		for (int j = i + 1; j < n; ++j) {
			if (ans[j] < ans[i]) {
				cb[i] = max(cb[i], cb[j] + 1);
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		assert(a[i] == ca[i]);
		assert(b[i] == cb[i]);
	}
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cerr << i << endl;
		printf("Case #%d: ", i);
		work2();
	}
	return 0;
}
