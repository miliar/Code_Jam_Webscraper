#include <iostream>
#include <string>
#include <cstdio>
#include <deque>

using namespace std;

int arr[8][8] = {
	{0, 1, 2, 3, 4, 5, 6, 7},
	{1, 0, 3, 2, 5, 4, 7, 6},
	{2, 3, 1, 0, 6, 7, 5, 4},
	{3, 2, 0, 1, 7, 6, 4, 5},
	{4, 5, 7, 6, 1, 0, 2, 3},
	{5, 4, 6, 7, 0, 1, 3, 2},
	{6, 7, 4, 5, 3, 2, 1, 0},
	{7, 6, 5, 4, 2, 3, 0, 1}
};

int quat(char a) {
	switch (a) {
	case 'i':
		return 2;
		break;
	case 'j':
		return 4;
		break;
	case 'k':
		return 6;
		break;
	}
}

int quat_pot(int q, int n, bool &hi, bool &hj, bool &hk) {
	int p = n % 8; // quaternion group has order 8
	int ret = q;
	for (int i = 0; i < p - 1; i++) {
		ret = arr[ret][arr[0][q]];
		if (ret == 2) hi = true;
		else if (ret == 4) hj = true;
		else if (ret == 6) hk = true;
	}
	return ret;
}

deque<int> getdeque(int barr[], int n, int x) {
	deque<int> ret;
	for (int i = 0; i < x; i++) {
		for (int j = 0; j < n; j++) {
			ret.push_back(barr[j]);
		}
	}
	return ret;
}

bool ijk(deque<int> &dq) {
	// Iterate until we obtain an i from the left
	int curr = 0; int buff;
	bool i = false;
	while (!dq.empty() && !i) {
		buff = dq.front();
		dq.pop_front();
		curr = arr[curr][buff];
		if (curr == 2) i = true;
	}

	// Iterate until we obtain k from the right
	curr = 0;
	bool k = false;
	while (!dq.empty() && !k) {
		buff = dq.back();
		dq.pop_back();
		curr = arr[buff][curr];
		if (curr == 6) k = true;
	}

	// See if the rest evaluates to j
	curr = 0;
	while (!dq.empty()) {
		buff = dq.front();
		dq.pop_front();
		curr = arr[curr][buff];
	}

	return curr == 4;
}

int main() {
	freopen("out.txt", "w", stdout);
	freopen("in.in", "r", stdin);

	int T;
	cin >> T;

	int l, x; char input; int q, curr;
	int barr[10000];
	for (int i = 0; i < T; i++) {
		cin >> l >> x;
		cin.get(); // newline
		curr = 0;
		for (int j = 0; j < l; j++) {
			cin.get(input);
			q = quat(input);
			barr[j] = q;
		}
		cin.get(); // newline
		deque<int> dq = getdeque(barr, l, x);
		cout << "Case #" << i + 1 << ": ";
		if (ijk(dq)) cout << "YES";
		else cout << "NO";
		cout << endl;
	}

	return 0;
}