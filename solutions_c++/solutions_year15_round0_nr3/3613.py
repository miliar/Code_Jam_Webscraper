#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std;

int readIn() {
	char c;
	cin >> c;
	if (c == 'i')
		return 2;
	if (c == 'j')
		return 3;
	if (c == 'k')
		return 4;
	cout << "FUUUUU";
	return 0;
}

int mul[][4] = {
	{1, 2, 3, 4},
	{2,-1, 4,-3},
	{3,-4,-1, 2},
	{4, 3,-2,-1}
}; 

int multiply(int a, int b) {
	if ((a < 0 && b < 0) || (a > 0 && b > 0)) {
		return mul[abs(a)-1][abs(b)-1];
	} else {
		return -1 * mul[abs(a)-1][abs(b)-1];
	}
}

void doit() {
	int L, X;
	cin >> L;
	cin >> X;
	vector<int> nums(X * L);
	for (int i = 0; i < L; i++) {
		nums[i] = readIn();
	}
	for (int i = L; i < X*L; i++) {
		nums[i] = nums[i % L];
	}
	// cout << "Read shit in " << endl;
	// for (int i = 0; i < nums.size(); i++) {
	// 	cout << nums[i] << ' ';
	// }
	// cout << endl;
	int l = X*L;
	int r = 0;
	int p = 1;
	for (int i = 0; i < X*L; i++) {
		p = multiply(p, nums[i]);
		if (p == 2) {
			l = i;
			break;
		}
	}
	// cout << "l = " << l << endl;
	p = 1;
	for (int i = X*L - 1; i >= 0; i--) {
		p = multiply(nums[i], p);
		if (p == 4) {
			r = i;
			break;
		}
	}
	// cout << "r = " << r << endl;
	if (l >= r) {
		cout << "NO" << endl;
		return;
	}
	p = 1;
	for (int i = l+1; i < r; i++) {
		p = multiply(p, nums[i]);
	}
	if (p == 3) {
		cout << "YES" << endl;
		return;
	} else {
		cout << "NO" << endl;
		return;
	}
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		doit();
	}
	return 1;
}